import numpy as np


class DiscreteState:

    def __init__(self, shape):
        self.state = np.zeros(shape)

    def __getitem__(self, indices):
        return self.state[indices]

    def __setitem__(self, indices, value):
        self.state[indices] = value

    def reset(self):
        self.state = np.zeros(self.state.shape)

    def to_array(self):
        return self.state.ravel()

    def to_int(self):
        self.to_base_10(self.state.ravel(), 2)

    @staticmethod
    def to_base_10(values, base):
        num = 0
        power = 1
        for i in reversed(range(0, len(values))):
            num += values[i] * power
            power *= base
