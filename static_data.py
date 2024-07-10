import random
import math
import argparse
import gym
from collections import deque
import numpy as np
import cv2
def  generate_random_float(min_value, max_value):
    return random.uniform(min_value, max_value)
if __name__ == '__main__':
    env = gym.make("CartPole-v0", render_mode="rgb_array")
    init_state = env.reset()
    action = 0
    next_state, reward, done, info,five = env.step(action)
    deg = math.pi
    env.render()
    env.env.env.env.state = np.array([-2.4, 0, deg, 0])
    env.render()
    min_rad = -math.pi
    max_rad = math.pi
    min_x = -2.4
    max_x = 2.4
    for i in range(50000):
        if i%100 == 0:
            print(i)
        x =generate_random_float(min_x, max_x)
        deg = generate_random_float(min_rad, max_rad)
        real_deg =  math.degrees(deg)
        env.env.env.env.state = np.array([x, 0, deg, 0])

        img = env.render()
        formatted_deg = "{:.2f}".format(real_deg)
        formatted_x = "{:.2f}".format(x)

        cv2.imwrite('./data/train/'+formatted_x+'_'+formatted_deg+'.jpg', img[:, :, ::-1])
    for j in range(10000):
        if i % 100 == 0:
            print(i)
        x =generate_random_float(min_x, max_x)
        deg = generate_random_float(min_rad, max_rad)
        real_deg =  math.degrees(deg)
        env.env.env.env.state = np.array([x, 0, deg, 0])

        img = env.render()
        formatted_deg = "{:.2f}".format(real_deg)
        formatted_x = "{:.2f}".format(x)

        cv2.imwrite('./data/test/'+formatted_x+'_'+formatted_deg+'.jpg', img[:, :, ::-1])
    print("end")
