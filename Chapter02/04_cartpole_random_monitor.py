import gym


if __name__ == "__main__":
    env = gym.make("CartPole-v0", render_mode="rgb_array")
    env=gym.wrappers.RecordVideo(env, video_folder="Chapter02/recording") 
    #env = gym.wrappers.Monitor(env, "recording")

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        result=env.step(action)
        obs=result[0]
        reward=result[1]
        done = result[2]
        #obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
    env.close()
    env.env.close()
