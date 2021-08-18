import sys

sys.path.append('.')

import projectaile as pai

pipeline = pai.PIPELINE()

@pipeline.callable
@pai.preprocess(apply_on_target=False)
def copier(inp):
    print(inp)
    
copier('Hi', 'Mindy')

print(copier.__dict__)

print(pipeline.callables)