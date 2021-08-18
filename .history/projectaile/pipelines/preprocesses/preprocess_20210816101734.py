from functools import wraps

# base preprocess method
def preprocess(apply_on_target=False):
    def decor(func):
        func.__apply_prob__ = prob
        func.__callable_type__ = 'augmentation'
        func.__apply_on_target__ = apply_on_target
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decor