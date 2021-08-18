import sys

sys.path.append('.')

import projectaile as pai

pipeline = pai.PIPELINE()

@pipeline.callable
@pai.preprocess({'apply_probability' : 0.4})
def copier():
    print(x, y)
    
copier('Hi', 'Mindy')

print(copier.__dict__)

print(pipeline.callables)