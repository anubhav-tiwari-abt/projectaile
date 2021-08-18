'''
    ProjectAile pipeline module

'''

# imports
from functools import wraps

'''
    Pipeline Base Class. Create a pipeline with callables that are called and
    intermediate states can be logged or altered.
'''
class PIPELINE:
    def __init__(self):
        self.callables = {}
        self.states = {}
    
    def callable(self, callable_method):
        self.callables[callable_method.__name__] = callable_method
        @wraps(callable_method)
        def wrapper(*args, **kwargs):
            print(f'Adding Callable : {callable_method.__name__} to pipeline.')
            callable_method.__pipeline_order__ = len(self.callables.keys() + 1)
            callable_method.__pipeline_def__ = self.
            return callable_method(*args, **kwargs)
        
        return wrapper