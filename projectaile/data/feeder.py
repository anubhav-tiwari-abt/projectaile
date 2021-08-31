from projectaile.data.loaders import loaders

'''
    FEEDER : FEEDER class for getting batches from the loader
            and feeding them to the model trainer
'''
class FEEDER:
    def __init__(self, config, loader=None):
        self.config = config
        self.initialize(loader)
	
    def initialize(self, loader):
        if not loader:
            loader = self.get_loader(self.config.data.data_type)
		
        print('Loader Found : ', loader)
        if loader:
            self.loader = loader
            self.loader.initialize(self.config)
            self.loader.get_data_info()
        else:
            raise Exception('No Loader Found For {self.config.data.data_type}!, Please Implement One.')
            
        self.train_iterator = 0
        self.valid_iterator = 0
        

    '''
    get_loader : returns one of default loaders based on the input type in config
    '''
    def get_loader(self, dtype):
        if dtype in loaders.keys():
            return loaders[dtype]
        else:
            print('No Default Loader Found For Given Data Type! Please Implement A Custom Data Loader Or Look At The Existing Loaders.')
            return None

    '''
        get_batch : get the next batch of data and apply preprocessing and augmentations steps
        iterator : the iterator index for either train or valid batch (step)
        batch_size : the number of samples to load
    '''
    def get_batch(self, mode='train', iterator=0, batch_size=1, shuffle=False):
        return self.loader.load_batch(mode, iterator, batch_size, shuffle)
	
    '''
        get_train_batch : get next training batch
    '''
    def get_train_batch(self):
        shuffle = self.train_iterator == 0
        
        x, y, self.train_iterator = self.get_batch(
            'train',
            self.train_iterator,
            self.config.hyperparameters.train_batch_size,
            shuffle
        )

        return x, y

    '''
        get_valid_batch : get next validation batch
    '''
    def get_valid_batch(self):
        shuffle = self.valid_iterator == 0
        
        x, y, self.valid_iterator = self.get_batch(
            'valid',
            self.valid_iterator, 
            self.config.hyperparameters.valid_batch_size,
            shuffle
        )

        return x, y