
# from .fairaml import FairAutoML
from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fairlearn.metrics import MetricFrame
from fairlearn.metrics import equalized_odds_ratio
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import time
from sklearn.metrics import balanced_accuracy_score, roc_auc_score
from lightgbm import LGBMClassifier, LGBMRegressor
from fairlearn.reductions import ExponentiatedGradient, DemographicParity, EqualizedOdds
from flaml import AutoML
import argparse

class ModelPerformance:
    """
    The class stores various measurements about a model's performance
    """

    def __init__(self, model_name, accuracy, disparity, time_taken, by_group_acc, **kwargs):
        self._model_name = model_name
        self._accuracy = accuracy
        self._disparity = disparity
        self._time_taken = time_taken
        self._by_group_acc = by_group_acc

    @property
    def accuracy(self):
        return self._accuracy

    @property
    def disparity(self):
        return self._disparity

    @property
    def by_group_acc(self):
        return self._by_group_acc

    @property
    def time_taken(self):
        return self._time_taken

    @property
    def model_name(self):
        return self._model_name

    def show_results(self):
        print("%.10s, %.4f, %.3f, %.2f" % (self._model_name, self._accuracy, self._disparity, self._time_taken))


def get_bar_plot(results):
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
    labels = results.keys()
    # set height of bar
    acc = [results[k].accuracy for k in labels]
    disparity = [results[k].disparity for k in labels]
    # Set position of bar on X axis
    br1 = np.arange(len(acc))
    br2 = [x + barWidth for x in br1]
    # Make the plot
    plt.bar(br1, acc, color ='r', width = barWidth,
            edgecolor='grey', label='Accuracy')
    plt.bar(br2, disparity, color ='g', width = barWidth,
            edgecolor='grey', label='Disparity')
    
    # Adding Xticks
    plt.xlabel('Methods', fontweight ='bold', fontsize = 15)
    plt.ylabel('Results', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(acc))],
            labels)
    
    plt.legend()
    # plt.show()
    plt.savefig('res.pdf')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('benchmark', type=str, nargs='?', default='final',
    #                     help="The benchmark type to run as defined by default \
    #                     in resources/benchmarks/{benchmark}.yaml")
    # parser.add_argument('exp_config', type=str, nargs='?', default='test',
    #                     help="The constraint definition to use as defined by \
    #                     default in exp_config.yaml. Defaults to `test`.")
    # parser.add_argument('-d', '--dataset_list', metavar='dataset_list', nargs='*',
    #                     default=[], help="The specific dataset id (as defined in \
    #                     the benchmark file) to run. " "When an OpenML reference is \
    #                     used as benchmark, the dataset name should be used instead. "
    #                     "If not provided, all datasets from the benchmark will be run.")
    # parser.add_argument('-m', '--method_list', dest='method_list', nargs='*',
    #                     default=[], help="The method list")

    fairness_metric = 'EO'
    mitigation_method = ExponentiatedGradient

    ## ***********data preprocessing for adult********************
    dataset_id = 1590
    sentitive_attribute = 'sex'
    target_att_pos = '>50K'
    target_att_neg = '<=50K'
    revised_targets = {target_att_pos: 1, target_att_neg: 0}
    # get dataset
    """Load dataset"""
    data = fetch_openml(data_id=1590, as_frame=True)
    X_raw = data.data
    X = pd.get_dummies(data.data)
    y_true = (data.target == '>50K') * 1
    sex = data.data[sentitive_attribute]
    sex.value_counts()
    start_time = time.time()
    print(X_raw[0:5])
    from flaml.data import load_openml_dataset
    # train test split
    X_train, X_test, y_train, y_test = load_openml_dataset(dataset_id=1590, data_dir='./', random_state=0, dataset_format="dataframe")
    # preprocessing
    sex_train = X_train[sentitive_attribute]
    sex_train.value_counts()
    sex_test = X_test[sentitive_attribute]
    sex_test.value_counts()
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)
    y_test = y_test.replace(revised_targets)
    y_train = y_train.replace(revised_targets)

    learner_names = ['lgbm', 'flaml', 'fair_flaml', 'fair_lgbm']
    learners = {}
    results = {}
    learners['lgbm'] = LGBMClassifier()
    aml_settings = {
        "time_budget": 120,  # total running time in seconds
        "metric": 'accuracy',  # primary metrics for regression can be chosen from: ['mae','mse','r2']
        "estimator_list": ['lgbm'],  # list of ML learners; we tune lightgbm in this example
        "task": 'classification', 
        "log_file_name": 'adult_experiment.log',  # flaml log file
        }
    
    learners['fair_flaml'] = None
    # get constraint
    constraint = EqualizedOdds()
    learners['fair_lgbm'] = mitigation_method(LGBMClassifier(), EqualizedOdds())
    new_learner = None
    # for k, learner in learners.items():
    for k in learner_names:
        end_time = time.time()
        if 'fair_lgbm' in k:
            learner = mitigation_method(LGBMClassifier(), EqualizedOdds())
            learner.fit(X_train, y_train, sensitive_features=sex_train)
            learners[k] = learner
        elif 'flaml' == k:
            learner = AutoML()
            learner.fit(X_train, y_train, **aml_settings)
            print(learner.best_config)
        elif k == 'fair_flaml':
            aml_learner = AutoML()
            aml_learner.fit(X_train, y_train, **aml_settings)
            # print(aml_learner.best_config, aml_learner.model.model)
            learner = mitigation_method(aml_learner.model.model, EqualizedOdds())
            learner.fit(X_train, y_train, sensitive_features=sex_train)
        else:
            learner = LGBMClassifier()
            learner.fit(X_train, y_train)
        learners[k] = learner
        finish_time = time.time()
        # doing prediction
        y_test_pred = learner.predict(X_test)
        print(y_test_pred.shape, y_test.shape)
        accuracy = accuracy_score(y_test, y_test_pred)
        # balanced_accuracy = balanced_accuracy_score(y_test, y_test_pred)
        ds = equalized_odds_ratio(y_test, y_test_pred, sensitive_features=sex_test)
        # gm = MetricFrame(equalized_odds_ratio, y_test, y_test_pred, sensitive_features=sex_test)
        # gm = MetricFrame(accuracy_score, y_test, y_test_pred, sensitive_features=sex_test)
        print('============method name==========', k)
        # print(gm.overall)
        # print(gm.by_group)
        # print('disparity between groups:', gm.difference(method='between_groups'))
        print('accuracy', accuracy)
        print('equalized odds ratio', ds)
        time_taken = finish_time - start_time
        print('time taken:', time_taken)
        # results[k] = ModelPerformance(gm.overall, gm.difference(method='between_groups'), gm.by_group)
        results[k] = ModelPerformance(k, accuracy, ds, time_taken, None)
    print('Method name, Accuracy, Equalized odds, Total Time Taken', )
    for v in results.values():
        v.show_results()
    get_bar_plot(results)

    """
    TODO:
    Questions:
    1. How does the constraints play a role in the reduction ?
    2. How to measure how good/bad fairness is?
        Need a threshold? Or just the smaller disparity the better?
    3. How to measure the quality of the results (given the fact that there are more than one metric).
        See wether the model is a dominating choice, or is one of the pareto front choices
    """
    # python test/fairaml/run_fairaml.py 
    