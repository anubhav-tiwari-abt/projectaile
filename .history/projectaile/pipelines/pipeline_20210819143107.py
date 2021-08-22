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

        self.states = {}
        self.components = {}
        self.pipeline_type = pipeline_type
        self.logger = LOGGER()
        
    # Used to fetch prebuilt pipelines
    def _create_pipeline_from_config_(self, config):
        return
            
    '''
        callable : decorator to make a function into a pipeline callable component and
                associate important properties like the logger to it.
        
    '''
    def callable(self, callable_method):
        self._init_callable_(callable_method)
        @wraps(callable_method)
        def wrapper(*args, **kwargs):
            self.logger.log(f'Adding Callable : {callable_method.__name__} to {self.pipeline_type}')
            return callable_method(*args, **kwargs)
        
        return wrapper
    
    def run(self, x, y):
        for callable in self.callables:
            x, y = self.callables(x, y)
            
        return x, y