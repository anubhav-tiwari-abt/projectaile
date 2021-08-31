import rich

from projectaile.loggers import LOGGER
from projectaile.utils.validator import VALIDATOR

class BASE:
    def __init__(self, config, *args, **kwargs):
        self.config = config
        self.validator = VALIDATOR()
        
        isvalid, missing_fields = self.validator.validate(self.config, doctype='config')
        
        if isvalid:
            self.logger = LOGGER(self.config.config_params.logs_path)
        else:
            self.logger = LOGGER()
            self.logger.raise_exception('config', 'invalid_config', missing_fields)
            return None
        
    def log(self, message):
        self.logger.log(message)
        
    def raise_exception(self, exception):
        return self.logger.raise_exception(exception, locals())