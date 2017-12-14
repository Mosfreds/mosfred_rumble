import os
import numpy as np
from vindinium.bots import BaseBot
from vindinium.ai import Minimax
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from keras.models import Sequential
from keras.models import model_from_json
from observations.action_space import VindiniumMoveSpace

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory



__all__ = ['MosfredRumble']


class MosfredRumble(BaseBot):

    def __init__(self):
        self._ann = None


    def start(self):
        self.deserialize_ann()

    def move(self):
        pass

    def _end(self):
        #update neural network
        pass



    def serialize_ann(self, path='.', base_name='mosfred_rumble'):
        model = self._ann.to_json()
        with open("{}/{}.json".format(path, base_name), 'w') as json_file:
            json_file.write(model)
        self._ann.save_weights("{}/{}.h5".format(path, base_name))

    def deserialize_ann(self, path='.', base_name='mosfred_rumble'):
        with open("{}/{}.json".format(path, base_name), 'r') as json_file:
            _ann = model_from_json(json_file.read())
        _ann.load_weights("{}/{}.h5".format(path, base_name))


    def create_ann(self):
        self._ann = Sequential()
        num_actions = len(VindiniumMoveSpace.get_moves())
#        model.add(Flatten(input_shape=(1,) + gamestate.shape))
        self._ann.add(Dense(500, input_dim=50, activation='relu'))
        self._ann.add(Dense(500, activation='relu'))
        # model.add(Activation('relu'))
        self._ann.add(Dense(num_actions, activation='linear'))

    def use_ann(self):
        self._ann.predict()


    # def learn_online(self, env):
    #     nb_actions = env.action_space.n #todo auslagern
    #
    #     policy = EpsGreedyQPolicy()
    #     memory = SequentialMemory(limit=50000,
    #                               window_length=1)  # Sequential Memory merkt sich die Ergebnisse, der performten Aktionen
    #     dqn = DQNAgent(model=self._ann, nb_actions=nb_actions, memory=memory, nb_steps_warmup=1000,
    #                    target_model_update=1e-2, policy=policy)
    #     dqn.compile(Adam(lr=1e-3), metrics=['mse'])
    #     dqn.fit(env, nb_steps=5000, visualize=True, verbose=2)
    #
    #     #dqn.test(env, nb_episodes=5, visualize=True)