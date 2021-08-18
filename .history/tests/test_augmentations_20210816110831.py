import sys

sys.path.append('.')

import projectaile as pai

pipeline = pai.PIPELINE()

@pipeline.callable
@pai.augmentation({'apply_probability' : 0.3}, apply_on_target=False)
def copier(inp):
    print(inp)
    inp += '!'
    return inp
    
a, b = copier('Hi', 'Mindy')

print(f'Outputs : {a}, {b}')

print(copier.__dict__)

print(pipeline.callables)