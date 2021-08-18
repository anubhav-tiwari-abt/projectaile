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

# To export only the model and not the whole pipeline
model = model_pipeline.model

# model would be an instance of tf.keras.model or pytorch.nn.module or sklearn.model
# it can be used as a normal model of framework of your choice.

# if the model needs to be finetuned, just use the model_pipeline and initialize a data_pipeline
# and compile the model_pipeline like in the above example.
# the model can be modified and updated in the model_pipeline before compiling.

model