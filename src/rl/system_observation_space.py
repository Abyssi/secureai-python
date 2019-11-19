from gym import spaces
import numpy as np
from enum import Enum


class NodeState(Enum):
    active = 0
    updated = 1
    corrupted = 2
    vulnerable = 3


class SystemObservationSpace(spaces.Box):

    def __init__(self, topology):
        super(SystemObservationSpace, self).__init__(low=0, high=1, shape=(len(topology.nodes) * len(list(NodeState)), ), dtype=np.uint8)
