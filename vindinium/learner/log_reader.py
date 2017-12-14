
from vindinium.models import game 
import json

class LogReader:
    def __init__(self, io_Obj):
        self._file = io_Obj
        
    def __iter__(self):
        return self

    def __next__(self):
        l = self._file.readline()
        if not l:
            raise StopIteration
        while not l.startswith("data: "):
           l = self._file.readline()
        state = {'game':json.loads(l[6:])}
        return game.Game(state)

