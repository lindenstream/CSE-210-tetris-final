import constants
from piece import Piece

class BlockS(Piece):
    # The purpose of BlockS is to contain rotational instances and color of the block
    def __init__(self):
        super().__init__()
        self.instances = [[6, 7, 9, 10], [1, 5, 6, 10]]
        self.color = constants.GREEN