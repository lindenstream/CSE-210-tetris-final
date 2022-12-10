class Piece:
    # The purpose of piece is to contain getter methods for the Tetris game pieces
    #   and to serve as a parent class for each block
    def __init__(self):
        self.instances = []
        self.color = (0, 0, 0)

    def get_instances(self):
        return self.instances

    def get_color(self):
        return self.color