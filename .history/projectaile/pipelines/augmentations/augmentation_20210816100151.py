from functools import wraps

# base augmentation method
def augmentation(prob=0.5, func=None):
    func.__apply_prob__ = prob
    func.__callable_type__ = 'augmentation'
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper