from rl.system_observation_space import NodeState
from rl.system_state import SystemState

from rl.abs.terminate_function import TerminateFunction


class SystemTerminateFunction(TerminateFunction):

    def terminated(self, state: SystemState):
        for i in range(0, state.size()):
            if not state[i, NodeState.active] or not state[i, NodeState.updated] or not state[
                i, NodeState.vulnerable] or not state[i, NodeState.corrupted]:
                return False

        return True
