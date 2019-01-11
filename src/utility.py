import os
from pathlib import Path
import datetime

import gym
from gym.envs import register
from gym_BitFlipper.envs import BitFlipperEnv


def resources_dir():
    env_var_str = 'RESOURCES_DIR'
    assert env_var_str in os.environ
    return Path(os.environ[env_var_str])


def get_cur_time_str():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


def make_env_BitFlipper(n=10,space_seed=0):
    id = "BitFlipper"+str(n)+":"+str(space_seed)+"-v0"
    try:
        register(id=id,entry_point='gym_BitFlipper.envs:BitFlipperEnv',kwargs = {"space_seed":space_seed,"n":n})
    except:
        print("Environment with id = "+id+" already registered. Continuing with that environment.")

    env=gym.make(id)
    env.seed(0)

    return env


def make_env_GoalBitFlipper(n=10,space_seed=0):
    id = "GoalBitFlipper" + str(n) + ":" + str(space_seed) + "-v0"
    try:
        register(id=id, entry_point='gym_BitFlipper.envs:GoalBitFlipperEnv', kwargs={"space_seed": space_seed, "n": n})
    except:
        print("Environment with id = " + id + " already registered. Continuing with that environment.")

    env = gym.make(id)
    env.seed(0)

    return env