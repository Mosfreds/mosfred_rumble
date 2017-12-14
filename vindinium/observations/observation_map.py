
import vindinium as vin

from vindinium.models.hero import Hero
from vindinium.models.map import Map
import vindinium.models.game as game

import numpy as np

class ObservationMap:

    def __init__(self, game):
        self.game = game
        self.map = None

    def observation_string(self):
        if self.map is None:
            translate_map(self)
        return np.array([j for i in self.map for j in i])
        
    def translate_map(self):
        game = self.game
        self.map = game.map
        
        #for my_mine in 
        
        
