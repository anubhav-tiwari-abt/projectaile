import sys

sys.path.append('.')

import projectaile as pai

pipeline = PIPELINE()

@pipeline.callable
@pai.preprocess()
def copier(x, y):
    print(x, y)
    
copier('Hi', 'Mindy'