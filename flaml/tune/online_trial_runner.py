import time
import numpy as np
import math
import logging
from .trial import Trial
from ray.tune.schedulers.trial_scheduler import TrialScheduler

# from config_aml import WARMSTART_NUM
logger = logging.getLogger(__name__)
RANDOM_SEED = 123456
WARMSTART_NUM = 100


class OnlineTrialRunner:
    """Implement a base online trial runner

    Args:
        searcher 
        scheduler
        test_policy: str 
    NOTE:
    --------------------------------
    APIs needed from the schedulers (schedulers that can be used for now: 
    FIFOScheduler, HyberbandScheduler, and OnlineDoublingScheduler). 
    1. on_trial_add(self, trial_runner: "trial_runner.TrialRunner", trial: Trial)
        It add candidate trials to the scheduler. It is called inside of the add_trial 
        function in the TrialRunner. 
    2. on_trial_remove(self, trial_runner: "trial_runner.TrialRunner", trial: Trial)
        Remove terminated trials from the scheduler.
    3. on_trial_result(self, trial_runner: "trial_runner.TrialRunner", trial: Trial, result: Dict)
        Reprot results to the scheduler.

    4. choose_trial_to_run(self, trial_runner: "trial_runner.TrialRunner") -> Optional[Trial]
    The last one, i.e., choose_trial_to_run is the most important function 
    ---------------------------------
    APIs needed from the searcher
    next_trial()
        Generate the next trial to add
    on_trial_result(self, trial_id: str, result: Dict)
        Reprot results to the scheduler.
    ---------------------------
    NOTE: About the status of a trial:
    PENDING: it indicates the trial is a candidate trial 
        when the scheduler choose the next trial to run. 
        All trials are set to be pending when frist added.
    RUNNING: it indicates that this trial is one of the concurrently running trials.
        The max number of RUNNING trials is running_budget.
    PAUSED: the status of a trial is set to PAUSED once it is removed from the running trials. 
        (The status of a PAUSED trial will be set to RUNNING the next time it selected to run? 
        The priority of the PAUSED trials is lower than the PENDING ones. )
    TERMINATED: set the status of a trial to TERMINATED when you never want to select it. 
        Trial.PENDING <=> resource_used == 0
        Trial.RUNNING  <=>  resource_used !=0 and the trial is running
        Trial.PAUSED  <=>  resource_used !=0 and the trial is not running
        Trial.TERMINATED  <=>  resource_used !=0 and the trial is not running and the trial has been pruned

    NOTE: in order to better keep track of the status of a trial, should only change the trial status in trial_runner 

    -----------------------------
    NOTE: About searcher and scheduler.
    1. The relationship between a trial_runner, which is an instance of the OnlineTrialRunner
    and searcher and scheduler.
    - trial_runner: with the help of searcher and the scheduler, it outputs a number of trials 
    to run when the caller calls the schedule_trials_to_run()
    - searcher: it is responsible to add new trials into trial_runner._trials.
    - scheduler: it is responsible to schedule the trials that exist in in trial_runner._trials. 

    Extreme case 1: all possible trials are added up front when the trail_runner is instanciated. 
    Then the trial_runner is just using the scheduler to schedule trials to run.

    Extreme case 2: everytime the trial_runner needs schedule a trial to run, it calls the searcher 
    to generate a new trial. Then the scheduler is not used. Examples: in the batch setting where the 
    evaluation of a trial is the training and validation on a fixed dataset, each config only needs to 
    be scheduled for batch evaluation for once.
    """

    def __init__(self,
                 max_live_model_num: int,
                 searcher=None,
                 scheduler=None,
                 champion_test_policy='loss_ucb',
                 **kwargs
                 ):
        # OnlineTrialRunner setting
        self._searcher = searcher
        self._scheduler = scheduler
        self._champion_test_policy = champion_test_policy
        self._max_live_model_num = max_live_model_num
        self._remove_worse = kwargs.get('remove_worse', True)
        self._bound_trial_num = kwargs.get('bound_trial_num', False)
        self._no_model_persistence = True

        # stores all the trials added to the OnlineTrialRunner
        # i.e., include the champion and all the challengers
        self._trials = []
        self._champion_trial = None
        self._best_challenger_trial = None
        self._first_challenger_pool_size = None
        self._random_state = np.random.RandomState(RANDOM_SEED)
        self._running_trials = set()

        # initially schedule up to max_live_model_num of live models and
        # set the first trial as the champion (which is done inside self.step())
        self._total_steps = 0
        logger.info('init step %s', self._max_live_model_num)
        self.step(self._max_live_model_num)
        assert self._champion_trial is not None

    @property
    def all_new_challengers_added(self) -> bool:
        return self._all_new_challengers_added

    @property
    def champion_trial(self) -> Trial:
        return self._champion_trial

    @property
    def best_challenger_trial(self) -> str:
        return self._best_challenger_trial

    @property
    def get_running_trials(self):
        return self._running_trials

    def step(self, max_live_model_num, data_sample=None, prediction_trial_tuple=None):
        """Schedule up to max_live_model_num trials to run

        It consists of the following several parts:
        Update model:
        0. Update running trials using observations received.
        Tests for Champion
        1. Test for champion (BetterThan test, and WorseThan test)
            1.1 BetterThan test
            1.2 WorseThan test: a trial may be removed if WroseThan test is triggered
        Online Scheduling:
        2. Report results to the searcher and scheduler (the scheduler will return a decision about
            the status of the running trials).
        3. Pause or stop a trial according to the scheduler's decision. 
           Add trial into the OnlineTrialRunner if there are opening slots.
        """
        # ***********Update running trials with observation***************************
        if data_sample is not None:
            self._total_steps += 1
            prediction_made = prediction_trial_tuple[0]
            prediction_trial = prediction_trial_tuple[1]
            if prediction_trial.status != Trial.RUNNING:
                print(prediction_trial.trial_id, self._champion_trial.trial_id)
            # assert prediction_trial.status == Trial.RUNNING
            trials_to_pause = []
            for trial in list(self._running_trials):
                if trial != prediction_trial:
                    y_predicted = trial.predict(data_sample)
                else:
                    y_predicted = prediction_made
                trial.train_eval_model_online(data_sample, y_predicted)
                logger.debug('running trial at iter %s %s %s %s %s %s', self._total_steps, trial.trial_id,
                             trial.result.loss_avg, trial.result.loss_cb, trial.result.resource_used, trial.resource_lease)  
                # report result to the searcher
                self._searcher.on_trial_result(trial.trial_id, trial.result)
                # report result the scheduler and the scheduler makes a decision about
                # the running status of the trial
                decision = self._scheduler.on_trial_result(self, trial, trial.result)
                # set the status of the trial according to the decision made by the scheduler
                logger.debug('trial decision %s %s at step %s', decision, trial.trial_id, self._total_steps)
                if decision == TrialScheduler.STOP:
                    self.stop_trial(trial)
                elif decision == TrialScheduler.PAUSE:
                    trials_to_pause.append(trial)
                else:
                    self.run_trial(trial)
            # ***********Statistical test of champion*************************************
            self._champion_test(max_live_model_num)
            # Pause the trial after the tests because the tests involves the reset of the trial's result
            for trial in trials_to_pause:
                self.pause_trial(trial)
        # ***********Add and schedule new trials to run if there are opening slots****
        # Add trial if needed: add challengers into consideration through _add_trial_from_searcher()
        # if there are available slots
        for _ in range(max_live_model_num - len(self._running_trials)):
            self._add_trial_from_searcher()
        # Scheduling: schedule up to max_live_model_num number of trials to run (set the status as Trial.RUNNING)
        # while max_live_model_num > len([trial for trial in self._trials.values() if trial.status == Trial.RUNNING]):
        while max_live_model_num > len(self._running_trials):
            trial_to_run = self._scheduler.choose_trial_to_run(self)
            if trial_to_run is not None:
                self.run_trial(trial_to_run)
            else:
                break
  
    def get_top_running_trials(self, top_ratio=None, top_metric='ucb') -> list:
        """Get a list of trial ids, whose performance is among the top running trials
        """
        running_valid_trials = [trial for trial in self._running_trials if
                                trial.result is not None]
        if not running_valid_trials:
            return
        if top_ratio is None:
            top_number = 0
        elif isinstance(top_ratio, float):
            top_number = math.ceil(len(running_valid_trials) * top_ratio)
        elif isinstance(top_ratio, str) and 'best' in top_ratio:
            top_number = 1
        else:
            raise NotImplementedError

        if 'ucb' in top_metric:
            test_attribute = 'loss_ucb'
        elif 'avg' in top_metric:
            test_attribute = 'loss_avg'
        elif 'lcb' in top_metric:
            test_attribute = 'loss_lcb'
        else:
            raise NotImplementedError
        top_running_valid_trials = []
        logger.info('Running trial ids %s', [trial.trial_id for trial in running_valid_trials])
        self._random_state.shuffle(running_valid_trials)
        results = [trial.result.get_score(test_attribute) for trial in running_valid_trials]
        sorted_index = np.argsort(np.array(results))  # sorted result (small to large) index
        for i in range(min(top_number, len(running_valid_trials))):
            top_running_valid_trials.append(running_valid_trials[sorted_index[i]])
        logger.info('Top running ids %s', [trial.trial_id for trial in top_running_valid_trials])
        return top_running_valid_trials

    def _add_trial_from_searcher(self):
        """Adds a new trial to this TrialRunner.

        The new trial is acquired from the input search algorithm, i.e. self._searcher
        A 'new' trial means the trial is not in self._trial
        """
        # (optionally) upper bound the number of trials in the OnlineTrialRunner
        if self._bound_trial_num and self._first_challenger_pool_size is not None:
            active_trial_size = len([t for t in self._trials if t.status != Trial.TERMINATED])
            trial_num_upper_bound = int(round((np.log10(self._total_steps) + 1) * self._first_challenger_pool_size)
                                        ) if self._first_challenger_pool_size else np.inf
            if active_trial_size > trial_num_upper_bound:
                logger.info('Do not add new trials: %s exceed trial limit %s.',
                            active_trial_size, trial_num_upper_bound)
                return None

        # output one trial from the trial pool (new challenger pool) maintained in the searcher
        # Assumption on the searcher: when all frontiers (i.e., all the challengers generated
        # based on the current champion) of the current champion are added, calling next_trial()
        # will return None
        trial = self._searcher.next_trial()
        if trial is not None:
            self.add_trial(trial)  # dup checked in add_trial
            # the champion_trial is initially None, so we need to set up it the first time
            # a valid trial is added.
            # Assumption on self._searcher: the first trial generated is the champion trial
            if self._champion_trial is None:
                logger.info('Initial set up of the champion trial %s', trial.config)
                self._set_champion(trial)
        else:
            self._all_new_challengers_added = True
            if self._first_challenger_pool_size is None:
                self._first_challenger_pool_size = len(self._trials)

    def _champion_test(self, max_live_model_num):
        # for BetterThan test, we only need to compare the best challenger with the champion
        self._get_best_challenger()
        if self._best_challenger_trial is not None:
            assert self._best_challenger_trial.trial_id != self._champion_trial.trial_id
            # test whether a new champion is found and set the trial properties accordingly
            is_new_champion_found = self._better_than_champion_test(self._best_challenger_trial)
            if is_new_champion_found:
                self._set_champion(new_champion_trial=self._best_challenger_trial)

        # performs WorseThan test, which is an optional compontent in ChaCha
        if self._remove_worse:
            to_stop = []
            active_trials = [t for t in self._trials if t.status != Trial.TERMINATED]
            for trial_to_test in self._trials:
                if trial_to_test.status != Trial.TERMINATED:
                    worse_than_champion = self._worse_than_champion_test(
                        self._champion_trial, trial_to_test)
                    if worse_than_champion:
                        to_stop.append(trial_to_test)
            # for trial in to_stop:
            #     self.stop_trial(trial)
            # TODO: we want to ensure there are at least #max_live_model_num of challengers remaining
            for i in range(min(len(active_trials) - max_live_model_num, len(to_stop))):
                self.stop_trial(to_stop[i])

    def _get_best_challenger(self):
        """Get the 'best' (in terms of the champion_test_policy) challenger under consideration.
        """
        # TODO: add a test metric in result
        if self._champion_test_policy is None:
            return
        if 'ucb' in self._champion_test_policy:
            test_attribute = 'loss_ucb'
        elif 'avg' in self._champion_test_policy:
            test_attribute = 'loss_avg'
        else:
            raise NotImplementedError
        #TODO: improve efficiency
        active_trials = [trial for trial in self._trials if
                         (trial.status != Trial.TERMINATED
                             and trial.trial_id != self._champion_trial.trial_id
                             and trial.result is not None)]
        if active_trials:
            self._random_state.shuffle(active_trials)
            results = [trial.result.get_score(test_attribute) for trial in active_trials]
            best_index = np.argmin(results)
            self._best_challenger_trial = active_trials[best_index]

    def _set_champion(self, new_champion_trial):
        """ Set the status of the existing trials once a new champion is found. 
        """
        assert new_champion_trial is not None
        is_init_update = False
        if self._champion_trial is None:
            is_init_update = True
        self.run_trial(new_champion_trial)
        # set the checked_under_current_champion status of the trials
        for trial in self._trials:
            if trial.trial_id == new_champion_trial.trial_id:
                trial.set_checked_under_current_champion(True)
            else:
                trial.set_checked_under_current_champion(False)
        self._champion_trial = new_champion_trial
        self._all_new_challengers_added = False
        logger.info('Set the champion  as %s', self._champion_trial.trial_id)
        if not is_init_update:
            self._champion_update_times += 1
            # calling set_search_properties of searcher will trigger new challenger generation
            # we do not do this for init champion this step is already done when first constructing the searcher
            self._searcher.set_search_properties(None, None, {self._searcher.CHAMPION_TRIAL_NAME: self._champion_trial})
        else:
            self._champion_update_times = 0

    def get_trials(self) -> list:
        """Returns the list of trials managed by this TrialRunner.

        Note that the caller usually should not mutate trial state directly.
        """
        return self._trials

    def add_trial(self, new_trial):
        """Adds a new trial to this TrialRunner.

        Trials may be added at any time.

        Args:
            trial (Trial): Trial to queue.
        NOTE: Even if the new trial already exisits, we still want to add a new trial because we want to reset 
        the status of the resouce consumption, such that we can replace bad ones in time. Otherwise, it is
        likely to get stuck on.

        Only add the new trial when it does not exist (according to the trial_id, which is the signature of
        the trail) in self._trials.
        """
        # Do not a trial with the same trial_id already exist, we do not add it directly.
        for trial in self._trials:
            if trial.trial_id == new_trial.trial_id:
                trial.set_checked_under_current_champion(True)
                return 
        logger.info('adding trial at iter %s, %s %s', self._total_steps, new_trial.trial_id, len(self._trials))
        self._trials.append(new_trial)  # do we need to check whether the trial exist
        # self._trials[new_trial.trial_id] = new_trial  # do we need to check whether the trial exist
        self._scheduler.on_trial_add(self, new_trial)

    def stop_trial(self, trial):
        """Stops trial.

        Trials may be stopped at any time. If trial is in state PENDING
        or PAUSED, calls `on_trial_remove`  for scheduler and
        `on_trial_complete() for searcher.    
        Otherwise waits for result for the trial and calls
        `on_trial_complete` for scheduler and searcher if RUNNING.
        """
        if trial.status in [Trial.ERROR, Trial.TERMINATED]:
            return
        else:
            logger.info('Terminating trial %s, with trial result %s',
                        trial.trial_id, trial.result)
            trial.set_status(Trial.TERMINATED)
            # clean up model and result
            trial.clean_up_model()
            self._scheduler.on_trial_remove(self, trial)
            self._searcher.on_trial_complete(trial.trial_id)
            self._running_trials.remove(trial)

    def pause_trial(self, trial):
        if trial.status in [Trial.ERROR, Trial.TERMINATED]:
            return
        else:
            logger.info('Pausing trial %s, with trial result %s %s %s %s',
                        trial.trial_id, trial.result.loss_avg,
                        trial.result.loss_cb, trial.result.loss_avg + trial.result.loss_cb, trial.resource_lease)
            logger.info('Current champion trial %s, with trial result %s %s %s %s',
                        self._champion_trial.trial_id, self._champion_trial.result.loss_avg,
                        self._champion_trial.result.loss_cb, self._champion_trial.result.loss_avg + self._champion_trial.result.loss_cb, + self._champion_trial.resource_lease)
            trial.set_status(Trial.PAUSED)
            # clean up model and result if no model persistence
            if self._no_model_persistence:
                trial.clean_up_model()
            self._running_trials.remove(trial)

    def run_trial(self, trial):
        if trial.status in [Trial.ERROR, Trial.TERMINATED]:
            return
        else:
            trial.set_status(Trial.RUNNING)
            self._running_trials.add(trial)

    def _better_than_champion_test(self, trial_to_test):
        """ test whether there is a config in the existing trials that is better than the 
        current champion config

        Returns: 
            new_champion_found: bool, which indicates whether a new champion is found 
            new_champion_trial:  which is the new champion found (it is None if 
                a new champion is not found)
        # when the result is None, it is not a live model, which means that we shoud not try to use it.
        # a non-live trial will only be scheduled to run in the scheduler, which does not need the 
        # result
        """
        if trial_to_test.result is not None and self._champion_trial.result is not None:
            if 'ucb' in self._champion_test_policy:
                return self._test_lcb_ucb(self._champion_trial, trial_to_test)
            elif 'avg' in self._champion_test_policy:
                return self._test_avg_loss(self._champion_trial, trial_to_test)
            elif 'martingale' in self._champion_test_policy:
                return self._test_martingale(self._champion_trial, trial_to_test)
            elif 'notest' in self._champion_test_policy:
                logger.info('no test')
                return False
        return False

    @staticmethod
    def _worse_than_champion_test(champion_trial, trial) -> bool:
        """Only considering one way of worse-than test
        """
        if trial.result is not None and trial.result.resource_used >= WARMSTART_NUM:
            if trial.result.loss_lcb - trial.result.loss_cb > champion_trial.result.loss_ucb:
                logger.info('=========trial %s is worse than champion %s=====',
                            trial.trial_id, champion_trial.trial_id)
                logger.info('trial %s %s %s', trial.config, trial.result, trial.resource_lease)
                logger.info('trial loss_avg:%s, trial loss_cb %s', trial.result.loss_avg, trial.result.loss_cb)
                logger.info('champion loss_avg:%s, champion loss_cb %s', champion_trial.result.loss_avg, champion_trial.result.loss_cb )
                logger.info('champion %s', champion_trial.config)
                logger.info('trial loss_avg_recent:%s, trial loss_cb %s', trial.result.loss_avg_recent, trial.result.loss_cb)
                logger.info('champion loss_avg_recent:%s, champion loss_cb %s', champion_trial.result.loss_avg_recent, champion_trial.result.loss_cb )
                return True
        return False

    @staticmethod
    def _test_lcb_ucb(champion_trial, trial) -> bool:
        """Comare the challenger(i.e., trial)'s loss upper bound with 
        champion_trial's loss lower bound - cb
        """
        assert trial.trial_id != champion_trial.trial_id
        if trial.result.resource_used >= WARMSTART_NUM:
            if trial.result.loss_ucb < champion_trial.result.loss_lcb - champion_trial.result.loss_cb:
                logger.info('=========new champion condition satisfied: using lcb vs ucb===========')
                logger.info('new champion trial %s %s %s',
                            trial.trial_id, trial.result.resource_used, trial.resource_lease)
                logger.info('new champion trial loss_avg:%s, trial loss_cb %s',
                            trial.result.loss_avg, trial.result.loss_cb)
                logger.info('old champion trial %s %s %s',
                            champion_trial.trial_id, champion_trial.result.resource_used,
                            champion_trial.resource_lease,)
                logger.info('old champion loss avg %s, loss cb %s',
                            champion_trial.result.loss_avg,
                            champion_trial.result.loss_cb)
                return True
        return False

    @staticmethod
    def _test_avg_loss(champion_trial, trial) -> bool:
        """Comare the challenger(i.e., trial)'s average loss with the
        champion_trial's average loss
        """
        assert trial.trial_id != champion_trial.trial_id
        if trial.result.resource_used >= WARMSTART_NUM:
            if trial.result.loss_avg < champion_trial.result.loss_avg:
                logger.info('=========new champion condition satisfied using avg loss===========')
                logger.info('trial %s', trial.config)
                logger.info('trial loss_avg:%s, trial loss_cb %s', trial.result.loss_avg, trial.result.loss_cb)
                logger.info('champion loss_avg:%s, champion loss_cb %s', champion_trial.result.loss_avg,
                            champion_trial.result.loss_cb)
                logger.info('champion %s', champion_trial.config)
                return True
        return False

    @staticmethod
    def _test_martingale(champion_trial, trial):
        """Comare the challenger and champion using confidence sequence based
        test martingale

        Not implementated yet
        """
        NotImplementedError


class OnlineBanditTrialRunner(OnlineTrialRunner):


    def step(self, max_live_model_num, data_sample=None, prediction_trial_tuple=None):
    
        """Schedule up to max_live_model_num bandit trials to run
        #TODO: revise the part about model udpate. 
        """
        pass