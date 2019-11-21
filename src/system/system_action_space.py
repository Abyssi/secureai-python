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
        self.max_execution_time = max([o.definition.execution_time for o in NodeAction])
        self.max_execution_cost = max([o.definition.execution_cost for o in NodeAction])
