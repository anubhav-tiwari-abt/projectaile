'''
    ProjectAile pipeline module

'''

# imports
from functools import wraps
from projectaile.loggers import LOGGER
from projectaile.savers import SAVER

'''
    Pipeline Base Class. Create a pipeline with callables that are called and
    intermediate states can be logged or altered.
'''
class PIPELINE:
    def __init__(self, from_config='', config=None, pipeline_type='data_pipeline'):
        if config:
            self._create_pipeline_from_config_(config)

        self.components = {}
        self.states = {}
        self.pipeline_type = pipeline_type
        self.logger = LOGGER()
        self.saver = SAVER()
        self.connection_channel = None
        self.threads = None
        self.distributed = False
        
    class COMPONENT:
        def __init__(self, callable, pipeline_def, pipeline_order):
            self.callable = callable
            self.__pipeline_def__ =  pipeline_def
            self.__pipeline_order__ = pipeline_order
            self.__execution_state__ = 'idle'
            self.__loop_iter_count__ = 0
            self.
        
    # Used to fetch prebuilt pipelines
    def _create_pipeline_from_config_(self, config):
        return
    
    def initialize(self):
        self.components = sorted(self.components, key=lambda x : x.__pipeline_order__)
        self.states = dict(zip([i.__pipeline_order__ for i in self.components], [None]*len(self.components.keys())))
        self.logger.log('')
    
    # Execute components in order of their pipeline order.        
    def run(self):
        for component in self.components:
            curr_comp = component.__pipeline_order__
            self.states[curr_comp] = component(self.states[curr_comp-1])
    
    