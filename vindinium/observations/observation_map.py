
import vindinium as vin

from vindinium.models.hero import Hero
from vindinium.models.map import Map
import vindinium.models.game as game

import numpy as np

class ObservationMap:

    def __init__(self, game):
        self.game = game
        self.map = None

    def _translate_map(self):
        game = self.game
        self.map = game.map
        for mine in game.mines:
            if not mine.owner is None:
                self.map[(mine.x, mine.y)] = vin.TILE_MINE_1 + mine.owner - 1
        for hero in game.heroes:
            self.map[(hero.x, hero.y)] = vin.TILE_BOT_1 + hero.id - 1

    def observation_string(self):
        if self.map is None:
            self._translate_map()
        m = []
        for i in range(0, self.map.size):
            for j in range(0, self.map.size):
                m.append(self.map[(i, j)])
        return m