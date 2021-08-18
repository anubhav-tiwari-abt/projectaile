import projectaile as pai

data_pipeline = pai.DATA_PIPELINE(from_config='object_detection', config_file='configs/config.yaml')

model_pipeline = pai.MODEL_PIPELINE(config_file='configs/config.yaml')

@model_pipeline.model
def compose_model():
    # returns tf.keras.model or pytorch.nn.module or sklearn.model
    return

@model_pipeline.callback
def save_state_on_cloud(model_state):
    pai.export_model(model_state)
    
@model_pipeline.callback
def log_to_remote_server(model_state):
    requests.post(model_state.logger.export_logs())
    
model_pipeline.compile(data_pipeline)

model_pipeline.run(save_only_best=True)

model_pipeline.save_state()


# On a different machine when importing

import projectaile as pai

model_pipeline = pai.MODEL_PIPELINE(from_state='model_state_path')

