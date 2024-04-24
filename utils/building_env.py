import numpy as np
import math

class ActionSpace(object):
    def __init__(self, n):
        self.n = n

    def sample(self):
        return np.random.randint(0, self.n)

class ObservationSpace(object):
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def sample(self):
        return tuple(np.random.randint(0, dim) for dim in self.dimensions)

class GridworldEnv:
    def __init__(self, width, length, height, beam_positions, origin, target):
        self.width = width
        self.length = length
        self.height = height
        self.state_size = (width, length, height)
        self.beam_positions = set(beam_positions)
        self.origin = origin
        self.target = target
        self.current_position = origin
        self.visited_states = [origin]
        
        self.action_space = ActionSpace(5)  # 5 possible actions: up, down, left, right, forward
        self.observation_space = ObservationSpace((width, length, height))

    def reset(self):
        self.current_position = self.origin
        self.visited_states = [self.origin]
        return self.observation_space.sample()

    def distance_3d(self, point1, point2):
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    def step(self, action):
        action = self.action_space.sample()  # Use the action space to determine the action
        x, y, z = self.current_position
        self.visited_states.append(self.current_position)
        previous_distance = self.distance_3d(self.current_position, self.target)
        movement = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (1, 0, 0)]
        dx, dy, dz = movement[action]
        x, y, z = x + dx, y + dy, z + dz
        x, y, z = min(max(x, 0), self.width-1), min(max(y, 0), self.length-1), min(max(z, 0), self.height-1)
        next_state = (x, y, z)

        current_distance = self.distance_3d(next_state, self.target)
        reward = -0.1  # Default slight penalty for moving
        if next_state == self.target:
            reward = 1  # reaching the target
        elif next_state in self.beam_positions:
            reward = -1  # collision with the beam
        elif current_distance < previous_distance:
            reward = 0.4
        elif next_state in self.visited_states:
            reward = -0.5  # visited state penalty
        elif next_state == self.current_position:
            reward = -1  # staying in the same cube

        self.current_position = next_state
        done = next_state == self.target
        return self.observation_space.sample(), reward, done

    def valid_actions(self):
        # All actions are valid in this setup
        return [0, 1, 2, 3, 4]

    def render(self):
        print(self.current_position)
