'''
    ProjectAile pipeline module

'''

# imports


'''
    Pipeline Base Class. Create a pipeline with callables that are called and
    intermediate states can be logged or altered.
'''
class PIPELINE:
    def __init__(self):
        self.callables = {}
        self.states = {}
    
    def initialize(self, ):
        return