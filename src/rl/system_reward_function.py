from rl.abs.reward_function import RewardFunction
from rl.system_action import SystemAction
from rl.system_action_space import SystemActionSpace
from rl.system_observation_space import SystemObservationSpace
from rl.system_state import SystemState


class SystemRewardFunction(RewardFunction):

    def __init__(self, action_space: SystemActionSpace, observation_space: SystemObservationSpace):
        self.action_space = action_space
        self.observation_space = observation_space

    def reward(self, old_state: SystemState, action: SystemAction, current_state: SystemState):
        -((action.node_action.definition.executrion_time / self.action_space.))