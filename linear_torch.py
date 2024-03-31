import torch
import torch.nn as nn
import torch.nn.functional as F

# from torch.tensor import Tensor
from torch import Tensor
from utils.test_env import EnvTest
from core.deep_q_learning_torch import DQN
from schedule import LinearExploration, LinearSchedule

from configs.q5_linear import config


class Linear(DQN):


    def initialize_models(self):

        # this information might be useful
        state_shape = list(self.env.observation_space.shape)
        img_height, img_width, n_channels = state_shape
        num_actions = self.env.action_space.n

        self.q_network = nn.Linear(img_height * img_width * n_channels * self.config.state_history, num_actions)
        self.target_network = nn.Linear(img_height * img_width * n_channels * self.config.state_history, num_actions)


    def get_q_values(self, state, network='q_network'):

        out = None

        state_f = torch.flatten(state, start_dim=1)
        network = getattr(self, network)
        out = network(state_f)

        return out


    def update_target(self):

        self.target_network.load_state_dict(self.q_network.state_dict())


    def calc_loss(self, q_values : Tensor, target_q_values : Tensor,
                    actions : Tensor, rewards: Tensor, done_mask: Tensor) -> Tensor:

        # you may need this variable
        num_actions = self.env.action_space.n
        gamma = self.config.gamma

        q_value = torch.gather(q_values, 1, actions.unsqueeze(1).long()).squeeze(1)
        max_next_q_value = target_q_values.max(1)[0]
        expected_q_value = rewards + gamma * max_next_q_value * (1 - done_mask.float())
        loss = torch.nn.functional.mse_loss(q_value, expected_q_value)
        return loss


    def add_optimizer(self):

        self.optimizer = torch.optim.Adam(self.q_network.parameters(), lr=self.config.lr_begin)




if __name__ == '__main__':
    env = EnvTest((5, 5, 1))

    # exploration strategy
    exp_schedule = LinearExploration(env, config.eps_begin,
            config.eps_end, config.eps_nsteps)

    # learning rate schedule
    lr_schedule  = LinearSchedule(config.lr_begin, config.lr_end,
            config.lr_nsteps)

    # train model
    model = Linear(env, config)
    model.run(exp_schedule, lr_schedule)