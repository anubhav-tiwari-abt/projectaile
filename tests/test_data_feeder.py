import sys

sys.path.append('./')

import projectaile as pai

config = pai.CONFIG('C:/Users/abtex/Desktop/projects/projectaile/projectaile/config/base_config.yaml')
feeder = pai.FEEDER(config)
print(feeder)