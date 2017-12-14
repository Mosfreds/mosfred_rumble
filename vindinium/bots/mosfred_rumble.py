import os
import numpy as np
from vindinium.bots import BaseBot
from vindinium.ai import Minimax
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from keras.models import Sequential
from keras.models import model_from_json
from observations.action_space import VindiniumMoveSpace



__all__ = ['MosfredRumble']


class MosfredRumble(BaseBot):
    _ann = None


    def serialize_ann(self, path='.', base_name='mosfred_rumble'):
        model = _ann.to_json()
        with open("{}/{}.json".format(path, base_name), 'w') as json_file:
            json_file.write(model)
        _ann.save_weights("{}/{}.h5".format(path, base_name))


    def deserialize_ann(self, path='.', base_name='mosfred_rumble'):
        with open("{}/{}.json".format(path, base_name), 'r') as json_file:
            _ann = model_from_json(json_file.read())
        _ann.load_weights("{}/{}.h5".format(path, base_name))


    def create_ann(self):
        model = Sequential()
        num_actions = len(VindiniumMoveSpace.moves)
#        model.add(Flatten(input_shape=(1,) + gamestate.shape))
        model.add(Dense(500, input_dim=50, activation='relu'))
        model.add(Dense(500, activation='relu'))
        # model.add(Activation('relu'))
        model.add(Dense(num_actions, activation='linear'))
        return model

