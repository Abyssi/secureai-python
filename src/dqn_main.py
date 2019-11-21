import gym
import tensorflow as tf
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import BoltzmannQPolicy
from tensorflow.keras.optimizers import Adam

from nn.nn_builder import NNBuilder
from utils.yaml import YAMLParser

tf.compat.v1.disable_eager_execution()


class DQNMain(object):
    @classmethod
    def main(cls, *args):
        topology = YAMLParser.parse("../../data/topology-1.yml")
        print(topology)

        env = gym.make('FrozenLake8x8-v0')
        model = NNBuilder().build(env.observation_space.shape, env.action_space.n)

        memory = SequentialMemory(limit=50000, window_length=1)
        policy = BoltzmannQPolicy()
        dqn = DQNAgent(model=model, nb_actions=env.action_space.n, memory=memory, nb_steps_warmup=40,
                       target_model_update=1e-2, policy=policy)
        dqn.compile(Adam(lr=1e-3), metrics=['mae'])

        dqn.fit(env, nb_steps=50000, visualize=True, verbose=2)

        dqn.save_weights('dqn_1_weights.h5f', overwrite=True)

        dqn.test(env, nb_episodes=5, visualize=True)


if __name__ == '__main__':
    import sys

    DQNMain.main(sys.argv)
