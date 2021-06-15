
def evaluate_loss(dataset, config):
    model = func(config)
    loss = get_loss(dataset, model)
    tune.report(metric=loss)


def evaluate_fair_loss(dataset, attribute, mitigation, fairness_metrics,
                       fairness_constraints, config)
    model = func(config)
    fair_model = mitigation(model, attribute, fairness_metrics, fairness_constraints)
    loss = get_loss(dataset, fair_model)
    tuen.report(metric=loss)


class FairAutoML:
    """The class for FairAutoMl
    """

    def __init__(self, dataset, fairness_metrics, fairness_constraints, mitigation, hpo_alg,
                 **automl_kwargs):
        """
        TODO:
            Check how to organize fairness_metrics and constraints
        """
        self._mitigation = mitigation
        self._automl_kwargs = automl_kwargs
        self.model = None
        self.fair_model = None

    def _get_dataset(self, dataset):
        """
        Dataset downloading and pre-processing
        """
        NotImplementedError

    def _get_fairness_score(self, test_data) -> float:
        """
        Get the fairness score on the model based on the test_data
        #TODO: maybe this should be a static method
        """
        score = None
        return score

    def _unfairness_mitigation(self):
        """
        Do the unfairness mitigation
        """
        self.fair_model = self._mitigation(self.model)

    def _hpo(self, do_mitigation):
        """
        Perform HPO and output the model
        """
        if not do_mitigation:
            trainable_func = partial(evaluate_loss, xxxx)
        else:
            trainable_func = partial(evaluate_fair_loss, xxxx)
        analysis = flaml.tune.run(self.hpo_alg, self.automl_kwargs)
        best_config = analysis.best_trial.best_config
        self.model = train(best_config)
        return self.model

    def post_aml_mitigation(self,):
        self._get_dataset()
        model = self._hpo()
        fair_model = self._unfairness_mitigation()
        return fair_model

    def on_aml_mitigation(self):
        return self._fair_hpo()
