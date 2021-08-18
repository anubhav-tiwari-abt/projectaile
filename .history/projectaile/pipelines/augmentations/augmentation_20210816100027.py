from functools import wraps

def augmentation(prob=0.5, func):
    def wrapper(func, *args, **kwargs):