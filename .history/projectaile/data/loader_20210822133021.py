class LOADER:
    def __init__(self, config):
        self.config = config
    
    '''
    get_data_info : extracts base information about the data for generating batches and using
                    it for getting batches of data from the feeders.
    '''
    # Getting indices and features and targets for the dataset.
    def get_dset_info(self):
        interface_type = self.config.c
            
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