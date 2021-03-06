"""
TODO:
1. add datasets (and dataset pre-processing) as part of the problem
2. add learners as part of the problem
"""
import logging
from flaml.tune import loguniform, uniform
from flaml.tune import polynomial_expansion_set
from flaml import AutoVW
logger = logging.getLogger(__name__)


class Problem:

    def __init__(self, **kwargs):
    self._setup_search()

    def _setup_search(self):
        self._search_space = {}
        self._init_config = {}

    @property
    def init_config(self):
        return self._init_config

    @property
    def search_space(self):
        return self._search_space


class VWTuning(Problem):

    def __init__(self, max_iter_num, dataset_id, ns_num, **kwargs):
        use_log = kwargs.get('use_log', True),
        shuffle = kwargs.get('shuffle', False)
        vw_format = kwargs.get('vw_format', True)
        from .data_to_vw import get_data
        print('dataset_id', dataset_id)
        self.vw_examples, self.Y = get_data(max_iter_num, data_source=dataset_id,
                                            vw_format=vw_format, max_ns_num=ns_num,
                                            shuffle=shuffle, use_log=use_log
                                            )
        self.max_iter_num = min(max_iter_num, len(self.Y))
        self._problem_info = {'max_iter_num': self.max_iter_num,
                              'dataset_id': dataset_id,
                              'ns_num': ns_num,
                             }
        self._problem_info.update(kwargs)
        self._fixed_hp_config = kwargs.get('fixed_hp_config', {})

    def _setup_search(self):
        """Set the search space and the initial config
        """
        self._search_space = {}
        self._init_config = {}
         
    @property
    def init_config(self):
        return self._init_config

    @property
    def search_space(self):
        return self._search_space


class VWNSInteractionTuning(VWTuning):

    def __init__(self, max_iter_num, dataset_id, ns_num, **kwargs):
        super().__init__(max_iter_num, dataset_id, ns_num, **kwargs)
        from flaml.onlineml import VowpalWabbitTrial
        self._raw_namespaces = list(AutoVW.get_ns_feature_dim_from_vw_example(self.vw_examples[0]).keys())
        self._info_key_list = ["dataset_id", "max_iter_num", "ns_num", "shuffle", "use_log"]
        self.problem_id = 'vw-ns-interaction-' + ('_').join(
            [str(self._problem_info.get(k, 'None')) for k in self._info_key_list])
        self._setup_search()
        logger.info('search space %s %s', self._search_space, self.problem_id)

    def _setup_search(self):
        # TODO: should be search space be a function or class?
        self._search_space = self._fixed_hp_config.copy()
        self._init_config = self._fixed_hp_config.copy()
        search_space = {'interactions': polynomial_expansion_set(
                                                       init_monomials=set(self._raw_namespaces),
                                                       highest_poly_order=len(self._raw_namespaces),
                                                       allow_self_inter=False),
                        }
        init_config = {'interactions': set()}
        self._search_space.update(search_space) 
        self._init_config.update(init_config)
        logger.info('search space %s %s %s', self._search_space, self._init_config, self._fixed_hp_config)

    @property
    def init_config(self):
        return self._init_config

    @property
    def search_space(self):
        return self._search_space


class VW_NS_LR(VWNSInteractionTuning):

    def __init__(self, max_iter_num, dataset_id, ns_num, **kwargs):
        super().__init__(max_iter_num, dataset_id, ns_num, **kwargs)
        self.problem_id = 'vw-ns-lr-' + ('_').join(
            [str(self._problem_info.get(k, 'None')) for k in self._info_key_list])
        self._setup_search()
        logger.info('search space %s', self._search_space)
        
    def _setup_search(self):
        self._search_space = self._fixed_hp_config.copy()
        self._init_config = self._fixed_hp_config.copy()
        search_space = {'interactions': polynomial_expansion_set(
                                                       init_monomials=set(self._raw_namespaces),
                                                       highest_poly_order=len(self._raw_namespaces),
                                                       allow_self_inter=False),
                                                    'learning_rate': loguniform(lower=2e-10, upper=1.0)
                        }
        init_config = {'interactions': set(), 'learning_rate': 0.5}
        self._search_space.update(search_space)
        self._init_config.update(init_config)
        logger.info('search space %s %s %s', self._search_space, self._init_config, self._fixed_hp_config)