from enum import Enum

from gym import spaces


class NodeAction(Enum):
    start = 0
    restart = 1
    update = 2
    heal = 3
    fix = 4


class SystemActionSpace(spaces.Discrete):

    def __init__(self, topology):
        super(SystemActionSpace, self).__init__((len(topology.nodes) * len(list(NodeAction))))
