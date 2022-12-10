import constants
from piece import Piece

class BlockO(Piece):
    # The purpose of BlockO is to contain rotational instances and color of the block
    def __init__(self):
        super().__init__()
        self.instances = [[1, 2, 5, 6]]
        self.color = constants.YELLOW