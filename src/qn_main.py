import gym

from rl.qlearning import QLearning
from utils.yaml import YAMLParser


class QNMain(object):
    @classmethod
    def main(cls, *args):
        topology = YAMLParser.parse("../../data/topology-1.yml")
        print(topology)

        env = gym.make('FrozenLake8x8-v0')

        ql = QLearning(env, .628, .9)

        ql.train()


if __name__ == '__main__':
    import sys

    QNMain.main(sys.argv)
