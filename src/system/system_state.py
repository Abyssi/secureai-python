import random

from rl.system_observation_space import NodeState

from rl.abs.discrete_state import DiscreteState


class SystemState(DiscreteState):

    def __init__(self, topology):
        super().__init__([topology.nodes.size(), len(list(NodeState))])

    def reset(self):
        super().reset()

        for i in range(0, self.size()):
            self[i, NodeState.active] = random.random < 0.7
            self[i, NodeState.updated] = random.random < 0.5
            self[i, NodeState.corrupted] = random.random > 0.6
            self[i, NodeState.vulnerable] = random.random > 0.7

    def worst(self):
        super().reset()

        for i in range(0, self.size()):
            self[i, NodeState.active] = False
            self[i, NodeState.updated] = False
            self[i, NodeState.corrupted] = True
            self[i, NodeState.vulnerable] = True

    def __setitem__(self, indices, value):
        super().__setitem__(indices, 1 if value else 0)
        return self

    def size(self):
        return self.state.shape[0]  # nodes count
