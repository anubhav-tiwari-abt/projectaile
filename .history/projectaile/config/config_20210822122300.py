import yaml
from yaml import Loader, Dumper
from configparser import ConfigParser

class DICTIONARY(dict):
    def __init__(self, **response):
        for k,v in response.items():
            if isinstance(v, dict):
                self.__dict__[k] = DICTIONARY(**v)
            else:
                self.__dict__[k] = v
                
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)
        
    def __len__(self):
        return len(self.__dict__)


class CONFIG(DICTIONARY):
    def __init__(self, config_file='./base_config.yaml', **kwargs):

        with open(config_file) as f:
            config = yaml.load(f, Loader=Loader)

        self.config = config

        for key, val in kwargs.items():
            config[key] = val

        super(CONFIG, self).__init__(**config)