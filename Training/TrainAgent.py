from ._train_agent import train_agent
from ._create_agent_and_env import create_agent_and_env

class TrainAgent():
	def __init__(self, **params):
		for k, v in params.items():
			setattr(self, k, v)
			
	def train_rl_agent(self, G, **kwargs):
		env, agent = create_agent_and_env(G, **self.__dict__)
		train_agent(env, agent, **self.__dict__)