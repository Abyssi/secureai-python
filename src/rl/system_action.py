from rl.system_state import SystemState


class SystemAction:
    def __init__(self, node_index, node_action):
        self.node_index = node_index
        self.node_action = node_action

    def run(self, system_state: SystemState):
        if self.node_action.definition.pre_node_state_function.run(system_state, self.node_index):
            self.node_action.definition.post_node_state_function.run(system_state, self.node_index)