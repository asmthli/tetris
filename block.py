import numpy as np


class Block:

    def __init__(self):
        self.grid_x_offset = 0
        self.grid_y_offset = 0
        self.rotation_offset = 0
        self.shape = None

    def get_grid_positions(self):
        positions = []
        for y in range(self.shape.shape[0]):
            for x in range(self.shape.shape[1]):
                binary = self.shape[y, x]
                if binary == 1:
                    offset_y = y + self.grid_y_offset
                    offset_x = x + self.grid_x_offset
                    positions.append((x, y))

        return positions

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def rotate(self):
        pass


class Square(Block):
    def __init__(self):
        super().__init__()
        self.colour = "yellow"
        self.shape = np.array([[1, 1, 0],
                               [1, 1, 0],
                               [0, 0, 0]])


class L(Block):
    def __init__(self):
        super().__init__()
        self.colour = "orange"
        self.shape = np.array([[1, 0, 0],
                               [1, 0, 0],
                               [1, 1, 0]])


class T(Block):
    def __init__(self):
        super().__init__()
        self.colour = "purple"
        self.shape = np.array([[0, 1, 0],
                               [1, 1, 1],
                               [0, 0, 0]])


class Z(Block):
    def __init__(self):
        super().__init__()
        self.colour = "green"
        self.shape = np.array([[1, 0, 0],
                               [1, 1, 0],
                               [0, 1, 0]])


class Line(Block):
    def __init__(self):
        super().__init__()
        self.colour = "blue"
        self.shape = np.array([[0, 1, 0],
                               [0, 1, 0],
                               [0, 1, 0]])


BLOCK_TYPES = [Square, Line, Z, L, T]
