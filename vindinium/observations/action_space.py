import random 
  
import gym, time
from gym.spaces import prng

import vindinium as vin

class VindiniumMoveSpace(gym.Space):
    """
    Action Space for Vindinium Moves 
    """
    directions = [vin.DIR_NORTH, vin.DIR_EAST, vin.DIR_SOUTH, vin.DIR_WEST, vin.DIR_STAY]
    moves =      [vin.NORTH,     vin.EAST,     vin.SOUTH,     vin.WEST,     vin.STAY]

    @classmethod
    def direction_to_move(cls, p):
        return cls.dirs[cls.directions.index((p[0],p[1]))]

    def move_to_direction(c):
         return cls.directions[cls.moves.index(c)]



     

    def sample(self):
        return random.choice(self.moves)
    
    def contains(self, x):
        return x in self.moves

    @classmethod
    def get_moves(cls):
        return cls.moves

    

    @property
    def shape(self):
        return ()
    def __repr__(self):
        return self.moves
    def __eq__(self, other):
        return self.moves == other.moves
