import heapq

# CONSTANTS
# tile values
TILE_EMPTY  = 0
TILE_WALL   = 1
TILE_SPAWN  = 2
TILE_TAVERN = 3
TILE_MINE   = 4

# command values
NORTH = 'North'
SOUTH = 'South'
WEST  = 'West'
EAST  = 'East'
STAY  = 'Stay'

# direction
DIR_NORTH = ( 0, -1)
DIR_SOUTH = ( 0,  1)
DIR_WEST  = (-1,  0)
DIR_EAST  = ( 1,  0)
DIR_STAY = ( 0, 0)


class HeapQueue(object):
    '''A priority queue implementation (it uses the heapq builtin module).
    Based on http://www.redblobgames.com/pathfinding/a-star/implementation.html
    '''

    def __init__(self):
        '''Constructor.'''
        self._queue = []
    
    def is_empty(self):
        '''Verifies if the queue is empty or not.
        
        Returns:
            (bool) whether if the queue is empty or not.
        '''
        return len(self._queue) == 0
    
    def push(self, item, priority):
        '''Pushes an item to the queue, given a priority.
        Args:
            item (object) any object.
            priority (int) a priority value.
        '''
        heapq.heappush(self._queue, (priority, item))
    
    def pop(self):
        '''Pops an item from the queue.
        Returns:
            (object) the stored item.
        '''
        return heapq.heappop(self._queue)[1]


class Map(object):
    '''Represents static elements in the game, such as walls, paths, taverns, 
    mines and spawn points.
    Attributes:
        size (int): the board size (in a single axis).
    '''
    
    def __init__(self, size):
        '''Constructor.
        
        Args:
            size (int): the board size.
        '''
        self.size = size
        self.__board = [[0 for i in range(size)] for j in range(size)]

    def __getitem__(self, key):
        '''Returns an item in the map.'''
        return self.__board[key[0]][key[1]]

    def __setitem__(self, key, value):
        '''Sets an item in the map.'''
        self.__board[key[0]][key[1]] = value

    def __str__(self):
        '''Pretty map.'''
        s = ' '
        s += '-'*(self.size) + '\n'
        for y in range(self.size):
            s += '|'
            for x in range(self.size):
                s += str(self[x, y] or ' ')
            s += '|\n'
        s += ' ' + '-'*(self.size)
        return s