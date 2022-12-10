import constants
from piece import Piece

class BlockL(Piece):
    # The purpose of BlockL is to contain rotational instances and color of the block
    def __init__(self):
        super().__init__()
        self.instances = [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]
        self.color = constants.ORANGE