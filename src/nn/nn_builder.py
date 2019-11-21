from keras import Sequential
from keras.layers import Dense, Activation


class NNBuilder:
    def build(self, inputs, outputs):
        model = Sequential()
        model.add(Dense(inputs))
        model.add(Activation('relu'))
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(outputs))
        model.add(Activation('linear'))
        return model
