import gym
from gym import spaces

from rl.system_action_space import SystemActionSpace
from rl.system_observation_space import SystemObservationSpace
from rl.system_state import SystemState


class SystemEnvironment(gym.Env):

    def __init__(self, topology):
        super(SystemEnvironment, self).__init__()
        self.action_space = SystemActionSpace(topology)
        self.observation_space = SystemObservationSpace(topology)
        self.state = SystemState(topology)  #np.env.observation_space.n

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass