import constants
from piece import Piece

class BlockJ(Piece):
    # The purpose of BlockJ is to contain rotational instances and color of the block
    def __init__(self):
        super().__init__()
        self.instances = [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]]
        self.color = constants.BLUE