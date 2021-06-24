'''Requirements if run exp that use deeptable model: 
conda create -n py37 python=3.7
pip install flaml[blendsearch,ray]
pip install tensorflow==2.2.0 deeptables[gpu]
pip install openml==0.9
pip install pandas==1.0
# pip install CondfigSpace hpbandster
# Find /lib/python3.7/site-packages/deeptables/preprocessing/transformer.py
#     # comment line 40:
#     # y = y.argmax(axis=-1)
'''

import time
import numpy as np
from flaml import tune
import pandas as pd
from functools import partial
import os
import logging
RANDOMSEED = 1024
try:
    import ray
    import flaml
    from flaml import BlendSearch
except ImportError:
    print("pip install flaml[blendsearch,ray,openml]")
logger = logging.getLogger(__name__)


def _test_problem_parallel(problem, time_budget_s=120, n_total_pu=4,
                           n_per_trial_pu=1, method='BlendSearch',
                           log_dir_address='logs/', log_file_name='logs/example.log',
                           ls_seed=20, report_intermediate_result=False, config_BS_in_flaml=True):
    metric = 'loss'
    mode = 'min'
    resources_per_trial = {"cpu": n_per_trial_pu, "gpu": 0}   # n_per_trial_pu
    open(log_file_name, "w")
    search_space = problem.search_space
    init_config = problem.init_config
    low_cost_partial_config = problem.low_cost_partial_config
    # specify pruning config
    prune_attr = problem.prune_attribute
    default_epochs, min_epochs, max_epochs = problem.prune_attribute_default_min_max  # 2**9, 2**1, 2**10
    cat_hp_cost = problem.cat_hp_cost
    reduction_factor_asha = 4
    reduction_factor_hyperband = 3
    start_time = time.time()
    # generate resource schedule for schedulers such as ASHA, hyperband, BOHB
    if 'ASHA' in method:
        resource_schedule = problem.generate_resource_schedule(reduction_factor_asha,
                                                               min_epochs, max_epochs)
    elif 'hyberband' in method or 'BOHB' in method:
        resource_schedule = problem.generate_resource_schedule(reduction_factor_hyperband,
                                                               min_epochs, max_epochs)
    else:
        # not tuning resource dim
        resource_schedule = [max_epochs]
    min_resource = resource_schedule[0]
    max_resource = resource_schedule[-1]

    # setup the trainable function
    ## TODO: specify the trainable_func through the AutoML problem
    trainable_func = partial(problem.trainable_func, start_time=start_time,
                             resource_schedule=resource_schedule, log_file_name=log_file_name, 
                             total_budget=time_budget_s)

    # specify how many total concurrent trials are allowed
    ray.init(num_cpus=n_total_pu, num_gpus=0) #n_total_pu
    if isinstance(init_config, list):
        points_to_evaluate = init_config
    else:
        points_to_evaluate = [init_config]

    if 'BlendSearch' in method and config_BS_in_flaml:
        # the default search_alg is BlendSearch in flaml, which use Optuna as the global search learner
        # corresponding schedulers for BS are specified in flaml.tune.run
        analysis = tune.run(
            trainable_func,
            points_to_evaluate=points_to_evaluate,
            low_cost_partial_config=low_cost_partial_config,
            cat_hp_cost=cat_hp_cost,
            metric=metric,
            mode=mode,
            prune_attr=prune_attr,
            max_resource=max_resource,
            min_resource=min_resource,
            report_intermediate_result=report_intermediate_result,
            resources_per_trial=resources_per_trial,
            config=search_space,
            local_dir=log_dir_address,
            num_samples=-1,
            time_budget_s=time_budget_s,
            use_ray=True)
    else:
        from ray.tune.suggest import BasicVariantGenerator
        scheduler = algo = None
        if 'Optuna' in method:
            from ray.tune.suggest.optuna import OptunaSearch
            import optuna
            sampler = optuna.samplers.TPESampler(seed=RANDOMSEED+int(run_index))
            algo = OptunaSearch(
                points_to_evaluate=points_to_evaluate, 
                sampler=sampler,
                space=search_space, mode=mode, metric=metric)
        elif 'CFO' in method:
            from flaml import CFO
            algo = CFO(
                metric=metric,
                mode=mode,
                space=search_space,
                points_to_evaluate=points_to_evaluate, 
                low_cost_partial_config=low_cost_partial_config,
                cat_hp_cost=cat_hp_cost,
                seed=ls_seed,
                )
        elif 'Dragonfly' in method:
            # pip install dragonfly-opt
            # doesn't support categorical
            from ray.tune.suggest.dragonfly import DragonflySearch
            algo = DragonflySearch(
                points_to_evaluate=points_to_evaluate, 
                space=search_space, mode=mode, metric=metric)
        elif 'SkOpt' == method:
            # pip install scikit-optimize
            # TypeError: '<' not supported between instances of 'Version' and 'tuple'
            from ray.tune.suggest.skopt import SkOptSearch
            algo = SkOptSearch(
                points_to_evaluate=points_to_evaluate, 
                space=search_space, mode=mode, metric=metric)
        elif 'Nevergrad' == method:
            # pip install nevergrad
            from ray.tune.suggest.nevergrad import NevergradSearch
            import nevergrad as ng
            algo = NevergradSearch(
                points_to_evaluate=points_to_evaluate, 
                space=search_space, mode=mode, metric=metric,
                optimizer=ng.optimizers.OnePlusOne)
        elif 'ZOOpt' == method:
            # pip install -U zoopt
            # ValueError: ZOOpt does not support parameters of type `Float` with samplers of type `Quantized`
            from ray.tune.suggest.zoopt import ZOOptSearch
            algo = ZOOptSearch(
                points_to_evaluate=points_to_evaluate, 
                dim_dict=search_space, mode=mode, metric=metric,
             budget=1000000)
        elif 'Ax' == method:
            # pip install ax-platform sqlalchemy
            from ray.tune.suggest.ax import AxSearch
            algo = AxSearch(
                points_to_evaluate=points_to_evaluate, 
                space=search_space, mode=mode, metric=metric)
        elif 'HyperOpt' in method:
            # pip install -U hyperopt
            from ray.tune.suggest.hyperopt import HyperOptSearch
            algo = HyperOptSearch(
                points_to_evaluate=points_to_evaluate,
                space=search_space, mode=mode, metric=metric,
                random_state_seed=RANDOMSEED + int(run_index))           

        if 'BlendSearch' in method:
            from flaml import BlendSearch
            print('low_cost_partial_config BS', low_cost_partial_config)
            algo = BlendSearch(
                points_to_evaluate=points_to_evaluate, 
                low_cost_partial_config=low_cost_partial_config,
                cat_hp_cost=cat_hp_cost,
                global_search_alg=algo,
                space=search_space, mode=mode, metric=metric, 
                seed=ls_seed,
                )
        if 'ASHA' in method:
            from ray.tune.schedulers import ASHAScheduler
            scheduler = ASHAScheduler(time_attr=prune_attr,
                                      max_t=max_resource,
                                      grace_period=min_resource,
                                      reduction_factor=reduction_factor_asha,
                                      )
            if 'ASHA' == method:
                algo = BasicVariantGenerator(points_to_evaluate=points_to_evaluate)
                scheduler = ASHAScheduler(time_attr=prune_attr,
                                          max_t=max_resource,
                                          grace_period=min_resource,
                                          reduction_factor=reduction_factor_asha,
                                          mode=mode, metric=metric
                                          )
                mode = None
                metric = None

        if 'BOHB' == method:
            from ray.tune.schedulers import HyperBandForBOHB
            from ray.tune.suggest.bohb import TuneBOHB
            algo = TuneBOHB() # points_to_evaluate=[init_config] 
            scheduler = HyperBandForBOHB(
                time_attr=prune_attr,
                max_t=max_resource,
                reduction_factor=reduction_factor_hyperband,
                )

        analysis = tune.run(trainable_func,
                            resources_per_trial=resources_per_trial,
                            config=search_space,
                            local_dir=log_dir_address,
                            num_samples=-1,
                            time_budget_s=time_budget_s,
                            verbose=1,
                            search_alg=algo
                            )

    metric = 'loss'
    mode = 'min'
    best_trial = analysis.get_best_trial(metric, mode, "all")
    loss = best_trial.metric_analysis[metric][mode]
    logger.info(f"method={method}")
    logger.info(f"dataset={oml_dataset}")
    logger.info(f"time={time.time()-start_time}")
    logger.info(f"Best model eval loss: {loss:.4f}")
    logger.info(f"Best model parameters: {best_trial.config}")


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import argparse
    from visualization import get_agg_lc_from_file, plot_lc
    from problems.aml_problem import AutoMLProblem
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', metavar='time', type=float, default=60, help="time_budget")
    parser.add_argument('-total_pu', '--n_total_pu', metavar='n_total_pu', type=int, default=26,
                        help="total number of gpu or cpu")
    parser.add_argument('-trial_pu', '--n_per_trial_pu', metavar='n_per_trial_pu', type=int, default=1,
                        help="number of gpu or cpu per trial")
    parser.add_argument('-l', '--learner_name', metavar='learner_name', type=str, default='dt', help="specify learner name")
    parser.add_argument('-r', '--run_indexes', dest='run_indexes', nargs='*', default=[0], help="The list of run indexes")
    parser.add_argument('-m', '--method_list', dest='method_list', nargs='*', default= ['Optuna',], help="The method list")
        # e.g., ['Optuna', 'BlendSearch+Optuna', 'CFO', 'ASHA', 'BOHB',]
    parser.add_argument('-d', '--dataset_list', dest='dataset_list', nargs='*', default=['vehicle'], help="The dataset list")
        # e.g., ['cnae','shuttle', ] 
    parser.add_argument('-plot_only', '--plot_only', action='store_true', help='whether to only generate plots.') 
    parser.add_argument('-agg', '--agg', action='store_true', help='whether to only agg lc.')
    args = parser.parse_args()
    time_budget_s = args.time
    # NOTE: do not differentiate gpu and cpu when configuring the resource (whether pu is gpu or cpu depends your machine)
    n_total_pu = args.n_total_pu
    n_per_trial_pu = args.n_per_trial_pu
    method_list = args.method_list
    dataset_list = args.dataset_list
    run_indexes = args.run_indexes
    learner_name = args.learner_name
    cwd = os.getcwd()
    log_dir_address = cwd + f'/logs/{learner_name}/'
    fig_dir_address = cwd + f'/plots/{learner_name}/'
    os.makedirs(log_dir_address, exist_ok=True)
    os.makedirs(fig_dir_address, exist_ok=True)
    logger.addHandler(logging.FileHandler(log_dir_address + f'tune_{learner_name}.log'))
    logger.setLevel(logging.INFO)
    
    # specify the problem
    for oml_dataset in dataset_list:
        for method in method_list:
            exp_alias = f'{learner_name}_' + '_'.join(str(s) for s in [
                n_total_pu, n_per_trial_pu, oml_dataset, time_budget_s, method])
            if args.plot_only and args.agg:
                log_file_name_alias = log_dir_address + exp_alias
                get_agg_lc_from_file(log_file_name_alias, method_alias=method)
            for run_index in run_indexes:
                # get the optimization problem
                optimization_problem = AutoMLProblem(dataset=oml_dataset, estimator=learner_name, fold=int(run_index), 
                                              n_jobs=1, time_budget=None, resampling_strategy=None)
                exp_run_alias = exp_alias + '_' + str(run_index)
                log_file_name = log_dir_address + exp_run_alias + '.log'
                if args.plot_only:
                    if not args.agg:
                        plot_lc(log_file_name, name=method)
                else:
                    _test_problem_parallel(problem=optimization_problem, time_budget_s=time_budget_s,
                                           n_total_pu=n_total_pu, n_per_trial_pu=n_per_trial_pu,
                                           method=method, log_dir_address=log_dir_address, log_file_name=log_file_name,
                                           ls_seed=20 + int(run_index))
        if args.plot_only or args.agg:
            if args.agg:
                fig_alias = f'LC_{learner_name}_lc' + '_'.join(str(s) for s in [n_total_pu, n_per_trial_pu, oml_dataset, time_budget_s])
            else:
                fig_alias = f'LC_{learner_name}_lc' + '_'.join(str(s) for s in [n_total_pu, n_per_trial_pu, oml_dataset, time_budget_s, run_index])
            fig_name = fig_dir_address + fig_alias + '.pdf'
            plt.legend()
            plt.savefig(fig_name)

# example command line:
# python test/test_automl_exp.py  -t 1800.0 -l xgb_flaml_woinit -d car  -m BlendSearch_Depri -total_pu 4 -trial_pu 1  -r 3