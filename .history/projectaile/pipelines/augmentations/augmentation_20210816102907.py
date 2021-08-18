from functools import wraps

# base augmentation method
def augmentation(config=None, apply_on_target=False):
    if config:
        # assign config vars to the function and use them
        # otherwise use defaults
        pass
    def decor(func):
        func.__apply_prob__ = prob
        func.__callable_type__ = 'augmentation'
        func.__apply_on_target__ = apply_on_target
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decor