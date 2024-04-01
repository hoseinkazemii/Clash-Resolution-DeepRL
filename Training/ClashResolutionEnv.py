import networkx as nx


# Define the RL Environment
class ClashResolutionEnv:
    def __init__(self, graph):
        self.graph = graph
        self.state = graph.copy()
        self.action_space = list(graph.edges)
        self.state_dim = len(graph.nodes)
        self.action_dim = len(self.action_space)

    def reset(self):
        return self.graph.copy()

    def step(self, action_idx):
        action = self.action_space[action_idx]
        # Perform the action (for simplicity, assume removing the edge)
        self.state.remove_edge(*action)
        # Calculate reward based on the number of remaining clashes
        reward = -len(nx.find_cliques(self.state))
        return self.state, reward