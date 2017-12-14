import gym
import random

import vindinium as vin

class VindiniumMoveSpace(gym.Space):
<<<<<<< HEAD
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



     
=======
    """ Action Space for Vindinium Moves """
    def __init__(self, n):
        self.moves = ["North", "East", "South", "West", "Stay"]
>>>>>>> 3f5f36c3f660dcd2dab17b8205068f2f2880ff50

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
