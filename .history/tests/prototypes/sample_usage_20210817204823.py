import projectaile as pai

pipeline = pai.PIPELINE(from_config='object_detection', config_file='configs/config.yaml')

data_feeder = pai.csv_feeder(config='configs/config.yaml')

data_loader = pai.LOADER(config='configs/config.yaml', feeder=data_feeder)

