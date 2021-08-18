import sys

sys.path.append('.')

from projectaile import PIPELINE

pipeline = PIPELINE()

@pipeline.callable
def name_func(name, class_):
    print(name, class_)
    
print(name_func)
print(name_func.__pipeline_order__)

name_func('Anubhav', '1')

pipeline.callables['name_func']('John', 'Wicked')