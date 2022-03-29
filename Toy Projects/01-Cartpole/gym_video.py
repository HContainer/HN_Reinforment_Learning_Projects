import gym

import custom_cartpole
env = gym.make('CustomCartPole-v0')
# env = gym.make('CartPole-v0')

max_ep = 10

for ep_cnt in range(max_ep):
    step_cnt = 0
    ep_reward = 0
    done = False
    state = env.reset()

    while not done:
        next_state, reward, done, _ = env.step(env.action_space.sample())
        env.render()
        step_cnt += 1
        ep_reward += reward
        state = next_state

    print('Episode: {}, Step count: {}, Eposide reward: {}'.format(ep_cnt, step_cnt, ep_reward))
env.close()


