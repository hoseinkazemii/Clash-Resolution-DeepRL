from .ClashResolutionEnv import ClashResolutionEnv
from .RLAgent import RLAgent



def create_agent_and_env(G, **params):

    # Create environment and agent
    env = ClashResolutionEnv(G)
    agent = RLAgent(env.state_dim, env.action_dim)

    return env, agent