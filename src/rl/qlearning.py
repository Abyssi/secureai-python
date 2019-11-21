import random

import gym
import numpy as np

from utils.stat import Stat


class QLearning:
    def __init__(self, mdp: gym.Env, learning_rate, discount_factor):
        self.q_table = np.random.rand(2 ** mdp.observation_space.n, mdp.action_space.size())
        self.mdp = mdp
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def train_step(self, state):
        action = self.choose(state)
        observation, reward, done, info = self.mdp.step(action)

        self.q_table[state, action] += self.learning_rate * (
                reward + self.discount_factor * np.max(self.q_table[observation]) - self.q_table[state, action])

        return observation, reward, done, info

    def choose(self, state):
        epsilon = 0.2
        if random.random <= epsilon:
            return self.mdp.action_space.random_action()

        return np.argmax(self.q_table[state])

    def train(self):
        stat = Stat("output/qlearning_1.csv")
        for i in range(0, 99):
            state = self.mdp.reset()
            for j in range(0, 99):
                if self.mdp.is_done():
                    break

                observation, reward, done, info = self.train_step(state)
                stat.append(reward)
