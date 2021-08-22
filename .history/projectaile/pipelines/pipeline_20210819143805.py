'''
    ProjectAile pipeline module

'''

# imports
from functools import wraps
from projectaile.loggers import LOGGER

'''
    Pipeline Base Class. Create a pipeline with callables that are called and
    intermediate states can be logged or altered.
'''
class PIPELINE:
    def __init__(self, config=None, pipeline_type='data_pipeline'):
        if config:
            self._create_pipeline_from_config_(config)

        self.components = {}
        self.states = {}
        self.pipeline_type = pipeline_type
        self.logger = LOGGER()
        
    # Used to fetch prebuilt pipelines
    def _create_pipeline_from_config_(self, config):
        return
    
    # Execute components in order of their pipeline order.        
    def run(self):
        executable_order = sorted(self.components, key=lambda x : x.__pipeline_order__)
        
        for component in self.components:
            