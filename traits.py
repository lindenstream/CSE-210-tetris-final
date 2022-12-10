import random
import constants
from blocki import BlockI
from blockj import BlockJ
from blockl import BlockL
from blocko import BlockO
from blocks import BlockS
from blockt import BlockT
from blockz import BlockZ

class Traits:
    # The purpose of Traits is to instantiate a list of block piece objects establish
    # imaging and rotating methods for the pieces
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
        self.color = random.randint(1, len(constants.COLORS) - 1)
        self.rotation = 0

    def image(self):
        # returns the current block instance and rotation
        return self.figures[self.type][self.rotation]

    def rotate(self):
        # sets a rotation for the game piece in question
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])