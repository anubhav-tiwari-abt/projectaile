import sys

sys.path.append('.')

import projectaile as pai

pipeline = PIPELINE()

@pipeline.callable
@pai.preprocess()
def 