import numpy as np
from functools import wraps

class LOADER:
    def __init__(self, loader_function):
        self._loader = loader_function
    
    '''
    get_data_info : extracts base information about the data for generating batches and using
                    it for getting batches of data from the feeders.
                
    '''
    
    def initialize(self, config):
        self._config = config
    
    # Getting indices and features and targets for the dataset.
    def get_data_info(self):
        if self._config.data.split == 0.0:
            interface_type = self._config.data.dataset.train.interface_type
        else:
            interface_type = self._config.data.dataset.interface_type
                
        if interface_type in extractors.keys():
            train_features, valid_features, train_targets, valid_targets = extractors[interface_type](self.config)
        else:
            print(f'Could not find a suitable extractor for the interface type : {interface_type}')
            exit(0)

        self.train_features = train_features
        self.train_targets = train_targets
        self.train_indices = np.arange(0, len(train_features))
        self.valid_features = valid_features
        self.valid_targets = valid_targets
        self.valid_indices = np.arange(0, len(valid_features))
    
    
    def load(self, feature, target):
        if self._config.data_type == 'structured':
            return feature, target
        else:
            if self._loader:
                return self._loader(feature, target)
            else:
                raise Exception('Not Implemented!, Implement a loader function for {self._config.data_type} data type.')
    
        
    def load_batch(self, mode='train', itertator=0, batch_size=1, shuffle=False):
        if mode == 'train':
            indices = self.train_indices
            features = self.train_features
            targets = self.train_targets
            
        elif mode == 'valid':
            indices = self.valid_indices
            features = self.valid_features
            targets = self.valid_targets
            
        if shuffle:
            indices = np.random.shuffle(indices)
        
        indices = indices[iterator*batch_size:(iterator+1)*batch_size]
        
        x, y = [], []
        
        for idx in indices:
            try:
                feature, target = self.load(features[idx], targets[idx])
                x.append(feature)
                y.append(target)
            except Exception as e:
                print(e)
                return None, None, iterator
        
        iterator += 1
        
        if iterator > len(indices)//batch_size:
            iterator = 0
            
        return np.array(x), np.array(y), iterator