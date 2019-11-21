class PreNodeStateFunction(object):
    def run(self, state, i):
        raise NotImplementedError("Should have implemented this")


class PostNodeStateFunction(object):
    def run(self, state, i):
        raise NotImplementedError("Should have implemented this")


class NodeActionDefinition:
    def __init__(self, execution_time, execution_cost, is_disruptive, pre_node_state_function: PreNodeStateFunction, post_node_state_function: PostNodeStateFunction):
        self.execution_time = execution_time
        self.execution_cost = execution_cost
        self.is_disruptive = is_disruptive
        self.pre_node_state_function = pre_node_state_function
        self.post_node_state_function = post_node_state_function

    def multiplied_by(self, factor):
        return NodeActionDefinition(self.execution_time * factor, self.execution_cost * factor, self.is_disruptive, self.pre_node_state_function, self.post_node_state_function)