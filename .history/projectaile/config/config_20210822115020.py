import yaml
from yaml import Loader, Dumper
from configparser import ConfigParser


class DICTIONARY:
    def __init__(self, **response):
        for k,v in response.items():
            if isinstance(v, dict):
                self.__dict__[k] = DICTIONARY(**v)
            else:
                self.__dict__[k] = v


class CONFIG(DICTIONARY):
    def __init__(self, config_file='./configs/config.cfg'):

        
        with open(config_file) as f:
            config = yaml.load(f)

        self.config = config

        for key, val in kwargs.items():
            config[key] = val

        super(CONFIG, self).__init__(**config)