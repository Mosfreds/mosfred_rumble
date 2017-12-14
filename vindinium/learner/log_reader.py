
from vindinium.models import game 
import json

class LogReader:
    def __init__(self, io_Obj):
        self.file = io_Obj
        
    def __iter__(self):
        return self

    def __next__(self):
        l = self.file.readline()
        if not l:
            raise StopIteration
        while not l.startswith("data: "):
               l = readline(self.file)
        state = {'game':json.load(l[6:])}
        return game.Game(state)

