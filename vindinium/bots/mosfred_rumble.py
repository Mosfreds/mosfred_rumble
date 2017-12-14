import os

from vindinium.bots import BaseBot
from vindinium.ai import Minimax

from keras.models import model_from_json



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