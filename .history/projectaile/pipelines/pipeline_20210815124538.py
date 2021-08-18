'''
    ProjectAile pipeline module

'''

# imports
from functools import wraps
from projectaile.loggers import Logger

'''
    Pipeline Base Class. Create a pipeline with callables that are called and
    intermediate states can be logged or altered.
'''
class PIPELINE:
    def __init__(self):
        self.callables = {}
        self.states = {}
        self.pipeline_type = 'data_pipeline'
        self.logger = None
    
    def _init_callable_(self, callable_method):
        callable_method.__pipeline_order__ = len(self.callables.keys()) + 1
        callable_method.__pipeline_def__ = self.pipeline_type
        callable_method.__log__ = True
        callable_method.__logger__ = self.logger
        callable_method.__return_state__ = True
    
    '''
        callable : decorator to make a function into a pipeline callable component and
                associate important properties like the logger to it.
        
    '''
    def callable(self, callable_method):
        self.callables[callable_method.__name__] = callable_method
        callable_method.__pipeline_order__ = len(self.callables.keys()) + 1
        callable_method.__pipeline_def__ = self.pipeline_type
        callable_method.__log__ = True
        callable_method.__logger__ = self.logger
        callable_method.__return_state__ = True
        @wraps(callable_method)
        def wrapper(*args, **kwargs):
            print(f'Adding Callable : {callable_method.__name__} to pipeline.')
            return callable_method(*args, **kwargs)
        
        return wrapper