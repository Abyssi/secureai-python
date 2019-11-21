import numpy as np
from keras import Model
from keras.layers import Dense


class DynNNBuilder:
    def __init__(self, model):
        self.model = model

    def add_outputs(self, n):
        output_layer = self.model.layers.pop()
        weights = output_layer.get_weights()

        shape = weights[0].shape[0]
        weights[1] = np.concatenate((weights[1], np.zeros(n)), axis=0)
        weights[0] = np.concatenate((weights[0], -0.0001 * np.random.random_sample((shape, n)) + 0.0001), axis=1)

        out = Dense(weights[1].shape[0], activation='softmax')(output_layer.input)
        new_model = Model(inputs=self.model.input, outputs=out)
        new_model.layers[-1].set_weights(weights)
        self.model = new_model
        return self

    def build(self):
        return self.model
