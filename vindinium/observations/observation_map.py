
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
            _translate_map(self)
        return np.array([j for i in self.map for j in i])
        
    def _translate_map(self):
        game = self.game
        self.map = game.map
        for mine in game.mines:
            if not mine.owner is None:
                self.map[mine.x][mine.y] = vin.TILE_MINE_1 + mine.owner - 1
        for hero in game.heroes:
            self.map[hero.x][hero.y] = vin.TILE_BOT_1 + hero.id - 1 
        #for my_mine in 
        
        
