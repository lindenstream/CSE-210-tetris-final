import constants
from piece import Piece

class BlockT(Piece):
    # The purpose of BlockT is to contain rotational instances and color of the T block
    def __init__(self):
        super().__init__()
        self.instances = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
        self.color = constants.PURPLE