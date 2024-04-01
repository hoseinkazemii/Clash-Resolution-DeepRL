from .QNetwork import QNetwork
import torch
import torch.nn as nn
import random
import torch.optim as optim

class RLAgent:
    def __init__(self, state_dim, action_dim, lr=0.001, gamma=0.99, epsilon=0.1):
        self.action_dim = action_dim
        self.q_network = QNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)
        self.gamma = gamma
        self.epsilon = epsilon

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_dim - 1)
        else:
            state_tensor = torch.FloatTensor(state)
            q_values = self.q_network(state_tensor)
            return torch.argmax(q_values).item()

    def update(self, state, action, reward, next_state):
        state_tensor = torch.FloatTensor(state)
        next_state_tensor = torch.FloatTensor(next_state)
        q_values = self.q_network(state_tensor)
        next_q_values = self.q_network(next_state_tensor)
        max_next_q_value = torch.max(next_q_values)
        target_q_value = reward + self.gamma * max_next_q_value
        loss = nn.MSELoss()(q_values[action], target_q_value)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()