import sys

sys.path.append('.')

import projectaile as pai

pipeline = pai.PIPELINE()

@pipeline.callable
@pai.preprocess()
def copier(x, y):
    print(x, y)
    
copier('Hi', 'Mindy')

print(copier.__dict__)

print(pipeline.callables)