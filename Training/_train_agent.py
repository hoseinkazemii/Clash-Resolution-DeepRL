# Training the RL Agent
def train_agent(env, agent, episodes=1000, **params):

    for episode in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
            if reward == 0:
                done = True
            
        print(f"Episode {episode + 1}/{episodes}, Reward: {reward}")