import yaml
from yaml import Loader, Dumper
from configparser import ConfigParser

class DICTIONARY(dict):
    def __init__(self, **response):
        self.store = dict()

        for k,v in response.items():
            if isinstance(v, dict):
                self.store[k] = DICTIONARY(**v)
            else:
                self.store[k] = v
                
    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)
        
    def __len__(self):
        return len(self.store)


class CONFIG(DICTIONARY):
    def __init__(self, config_file='./base_config.yaml', **kwargs):

        with open(config_file) as f:
            config = yaml.load(f, Loader=Loader)

        self.config = config

        for key, val in kwargs.items():
            config[key] = val

        super(CONFIG, self).__init__(**config)