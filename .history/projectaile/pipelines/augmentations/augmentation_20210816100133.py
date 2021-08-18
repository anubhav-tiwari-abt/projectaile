from functools import wraps

# base augmentation method
def augmentation(prob=0.5, func=None):
    func.__apply_prob__ = prob
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper