from .. import PIPELINE

pipeline = PIPELINE()

@pipeline.callable
def name_func(name, class_):
    print(name, class_)
    

name_func('Anubhav', '1')

pipeline.callables['name_func']('John', 'Wicked')