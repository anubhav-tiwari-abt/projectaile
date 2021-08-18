from functools import wraps

# base augmentation method
def augmentation(config:dict=None, apply_on_target:bool=False):
    if config:
        # assign config vars to the function and use them
        # otherwise use defaults
        pass
    def decor(func:function):
        func.__apply_prob__ = prob
        func.__callable_type__ = 'augmentation'
        func.__apply_on_target__ = apply_on_target
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decor