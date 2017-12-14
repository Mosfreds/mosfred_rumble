import random 
  
import gym, time
from gym.spaces import prng

class VindiniumMoveSpace(gym.Space):
    """
    Action Space for Vindinium Moves 
    """
    def __init__(self, n):
        self.moves = ["North", "East", "South", "West", "Stay"]

    def sample(self):
        return random.choice(self.moves)
    
    def contains(self, x):
        return x in self.moves

    @property
    def shape(self):
        return ()
    def __repr__(self):
        return self.moves
    def __eq__(self, other):
        return self.moves == other.moves
