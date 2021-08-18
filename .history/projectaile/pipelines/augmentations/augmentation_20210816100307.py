from functools import wraps

# base augmentation method
def augmentation(prob=0.5, apply_on_target=False, func=None):
    func.__apply_prob__ = prob
    func.__callable_type__ = 'augmentation'
    func.__apply_on_target__ = apply_on_target
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper