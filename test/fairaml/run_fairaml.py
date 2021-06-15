
# from .fairaml import FairAutoML
from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fairlearn.metrics import MetricFrame
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import time
from lightgbm import LGBMClassifier, LGBMRegressor
from fairlearn.reductions import ExponentiatedGradient, DemographicParity, EqualizedOdds
from flaml import AutoML


class ModelPerformance:
    """
    The class stores various measurements about a model's performance
    """

    def __init__(self, accuracy, disparity, by_group_acc, **kwargs):
        self._accuracy = accuracy
        self._disparity = disparity
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
    # get dataset
    """Load dataset"""
    data = fetch_openml(data_id=1590, as_frame=True)
    X_raw = data.data
    X = pd.get_dummies(data.data)
    y_true = (data.target == '>50K') * 1
    sex = data.data['sex']
    sex.value_counts()
    start_time = time.time()
    print(X_raw[0:5])
    from flaml.data import load_openml_dataset
    # train test split
    X_train, X_test, y_train, y_test = load_openml_dataset(dataset_id=1590, data_dir='./', random_state=0, dataset_format="dataframe")
    # preprocessing
    sex_train = X_train['sex']
    sex_train.value_counts()
    sex_test = X_test['sex']
    sex_test.value_counts()
    X_train = pd.get_dummies(X_train)
    X_test = pd.get_dummies(X_test)
    y_test = y_test.replace({'>50K': 1, '<=50K': 0})
    y_train = y_train.replace({'>50K': 1, '<=50K': 0})
    # #TODO: learning step
    # model = train_model()
    # y_pred = model.predict(X)
    # fairness_score = get_fairness_score(accuracy_score, y_true, y_pred, sensitive_features=sex)

    learners = {}
    results = {}
    learners['vanilla'] = LGBMClassifier()

    aml_settings = {
        "time_budget": 30,  # total running time in seconds
        "metric": 'accuracy',  # primary metrics for regression can be chosen from: ['mae','mse','r2']
        "estimator_list": ['lgbm'],  # list of ML learners; we tune lightgbm in this example
        "task": 'classification', 
        "log_file_name": 'adult_experiment.log',  # flaml log file
        }
    learners['flaml'] = AutoML()
    # learners['fair_flaml'] = None
    # # get constraint
    # # constraint = EqualizedOdds()
    # learners['mitigation'] = ExponentiatedGradient(LGBMClassifier(), EqualizedOdds())
    for k, learner in learners.items():
        end_time = time.time()
        if 'mitigation' in k:
            learner.fit(X_train, y_train, sensitive_features=sex_train)
        elif 'flaml' == k:
            learner.fit(X_train, y_train, **aml_settings)
            print(learner.best_config)
        elif k == 'fair_flaml':
            aml_learner = AutoML()
            aml_learner.fit(X_train, y_train, **aml_settings)
            print(aml_learner.best_config, aml_learner.model.model)
            learner = ExponentiatedGradient(aml_learner.model.model, EqualizedOdds())
            learner.fit(X_train, y_train, sensitive_features=sex_train)
        else:
            learner.fit(X_train, y_train)
        y_test_pred = learner.predict(X_test)
        finish_time = time.time()
        print(y_test_pred.shape, y_test.shape)
        gm = MetricFrame(accuracy_score, y_test, y_test_pred, sensitive_features=sex_test)
        print('============method name==========', k)
        print(gm.overall)
        print(gm.by_group)
        print('disparity between groups:', gm.difference(method='between_groups'))
        print('time taken:', finish_time-start_time)
        results[k] = ModelPerformance(gm.overall, gm.difference(method='between_groups'), gm.by_group)
    
    get_bar_plot(results)
    """
    TODO:
    1. How does the constraints play a role?
    2. How to measure the fairness of a model? 
    Need a threshold on the constraints? Or just the smaller disparity the better?
    """
    # python test/fairaml/run_fairaml.py 
    