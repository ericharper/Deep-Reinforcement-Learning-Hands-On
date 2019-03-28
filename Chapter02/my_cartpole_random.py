import gym

if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    env = gym.wrappers.Monitor(env, "recordings", force=True)
    total_reward = 0.0
    total_steps = 0
    total_games = 0
    obs = env.reset()

    while total_games < 10000:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1

        if done:
            total_games += 1
            env.reset()

    print(" Average %d steps, Average reward %.2f" % (1.0*total_steps / total_games, 1.0*total_reward / total_games))