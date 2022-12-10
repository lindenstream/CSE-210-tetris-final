import constants
from piece import Piece

class BlockI(Piece):
    # The purpose of BlockI is to contain rotational instances and color of the I block
    def __init__(self):
        super().__init__()
        self.instances = [[1, 5, 9, 13], [4, 5, 6, 7]]
        self.color = constants.TEAL