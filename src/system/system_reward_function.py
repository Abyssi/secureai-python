from rl.system_action import SystemAction
from rl.system_action_space import SystemActionSpace
from rl.system_observation_space import SystemObservationSpace
from rl.system_state import SystemState

from rl.abs.reward_function import RewardFunction


class SystemRewardFunction(RewardFunction):

    def __init__(self, action_space: SystemActionSpace, observation_space: SystemObservationSpace):
        self.action_space = action_space
        self.observation_space = observation_space

    def reward(self, old_state: SystemState, action: SystemAction, current_state: SystemState):
        return -((action.node_action.definition.execution_time / self.action_space.max_execution_time) + (
                action.node_action.definition.execution_cost / self.action_space.max_execution_cost)) * self.destruction(
            action, current_state)

    def destruction(self, action: SystemAction, current_state: SystemState):
        if not action.node_action.definition.is_disruptive:
            return 1 / current_state.size()

        if self.observation_space.replications(action.node_index) > 1:
            return 1 / current_state.size()

        return (self.observation_space.in_connections(action.node_index) + self.observation_space.out_connections(
            action.node_index)) / current_state.size()
