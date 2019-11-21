from enum import Enum

import numpy as np
from gym import spaces


class NodeState(Enum):
    active = 0
    updated = 1
    corrupted = 2
    vulnerable = 3


class SystemObservationSpace(spaces.Box):

    def __init__(self, topology):
        super(SystemObservationSpace, self).__init__(low=0, high=1, shape=(len(topology.nodes) * len(list(NodeState)),),
                                                     dtype=np.uint8)
        self.topology = topology

    def replications(self, node_index):
        return self.topology[node_index].replication

    def in_connections(self, node_index):
        return self.topology[node_index].in_edges

    def out_connections(self, node_index):
        return self.topology[node_index].out_edges
