import projectaile as pai

pipeline = pai.PIPELINE(from_config='object_detection', config_file='configs/config.yaml')

data_loader = pai.LOADER()

feeder = pai.csv_feeder(