import random
import constants
from blocki import BlockI
from blockj import BlockJ
from blockl import BlockL
from blocko import BlockO
from blocks import BlockS
from blockt import BlockT
from blockz import BlockZ

# The purpose of the class 'Traits' is to instantiate a list of block
# piece objects and establish imaging and rotating methods for the pieces

class Traits:
    
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        # initialize block objects
        self.bi = BlockI()
        self.bz = BlockZ()
        self.bs = BlockS()
        self.bj = BlockJ()
        self.bl = BlockL()
        self.bt = BlockT()
        self.bo = BlockO()
        # place block objects in a list
        self.figures = [
            self.bi.instances,
            self.bz.instances,
            self.bs.instances,
            self.bj.instances,
            self.bl.instances,
            self.bt.instances,
            self.bo.instances
        ]
        self.type = random.randint(0, len(self.figures) - 1)
        if self.type == 0:
            self.color = 1
        elif self.type == 1:
            self.color = 2
        elif self.type == 2:
            self.color = 3
        elif self.type == 3:
            self.color = 4
        elif self.type == 4:
            self.color = 5
        elif self.type == 5:
            self.color = 6
        elif self.type == 6:
            self.color = 7

        # self.color = random.randint(1, len(constants.COLORS) - 1)
        self.rotation = 0

    def image(self):
        # returns the current block instance and rotation
        return self.figures[self.type][self.rotation]

    def rotate(self):
        # sets a rotation for the game piece in question
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])