from projectaile import PIPELINE

pipeline = PIPELINE()

@pipeline.callable
def name_func(name, class_):
    print(name, class_)
    
