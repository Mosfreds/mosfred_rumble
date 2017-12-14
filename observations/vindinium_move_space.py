import random 
  
import gym, time
from gym.spaces import prng

class VindiniumMoveSpace(gym.Space):
    """
    Action Space for Vindinium Moves 
    """
    moves = ["North", "East", "South", "West", "Stay"]

    def sample(self):
        return random.choice(VindiniumMoveSpace.moves)
    
    def contains(self, x):
        return x in self.moves

    @staticmethod
    def get_moves():
        return VindiniumMoveSpace.moves

    @property
    def shape(self):
        return ()
    def __repr__(self):
        return self.moves
    def __eq__(self, other):
        return self.moves == other.moves
