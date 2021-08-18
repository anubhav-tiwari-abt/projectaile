import datetime

class LOGGER:
    def __init__(self):
        self.logger_name = 'general logger'
        pass
    
    def log(self, log_message):
        timestamp = datetime.datetime.now()
        log_str = f'{self.logger_name} : {timestamp} :\t {log_message}'
        print(log_str)