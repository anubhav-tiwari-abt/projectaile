from functools import wraps

# base preprocess method
def preprocess(config=None, apply_on_target=False):
    if config:
        # assign config vars to the function and use them
        # otherwise use defaults
        pass
    def decor(func):
        func.__callable_type__ = 'preprocess'
        func.__apply_on_target__ = apply_on_target
        @wraps(func)
        def wrapper(x, y, *args, **kwargs):
            def executor():
                func(
            func(*args, **kwargs)
        return wrapper
    return decor