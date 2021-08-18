class MODEL:
    def __init__(self, config, loader=None):
        self.config = config
        self.model = self.compose_model()
        self.compile(loader)

    def compile(self):
        self.feeder = FEEDER(self.config, loader)
        self.callbacks = CALLBACKS(self.config)
        self.trainer = TRAINER(self.config, self.model, self.feeder, self.callbacks)

    def train(self):
        self.trainer.train()

    def compose_model(self):
        return

    def train_step(self, x, y):
        return

    def summary(self):
        return

    def plot_model(self):
        return

    def save(self, only_weights=False):
        return

    def load(self, model_path='./models'):
        return

    def predict(self, x):
        return