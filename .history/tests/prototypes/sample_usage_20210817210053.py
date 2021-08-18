import projectaile as pai

data_pipeline = pai.DATA_PIPELINE(from_config='object_detection', config_file='configs/config.yaml')

model_pipeline = pai.MODEL_PIPELINE()

@model_pipeline.model
def compose_model():
    # returns tf.keras.model or pytorch.nn.module or sklearn.model
    return

model_pipeline.initialize(data_pipeline)