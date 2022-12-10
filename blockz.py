import constants
from piece import Piece

class BlockZ(Piece):
    # The purpose of BlockZ is to contain rotational instances and color of the Z block
    def __init__(self):
        super().__init__()
        self.instances = [[4, 5, 9, 10], [2, 6, 5, 9]]
        self.color = constants.RED