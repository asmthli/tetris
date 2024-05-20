import numpy as np


class Block:

    def __init__(self, x_offset):
        self.grid_x_offset = x_offset
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
                    positions.append((offset_x, offset_y))

        return positions

    def move_down(self):
        self.grid_y_offset += 1

    def move_left(self):
        self.grid_x_offset -= 1

    def move_right(self):
        self.grid_x_offset += 1

    def rotate(self):
        pass

    def check_for_collision(self, grid):
        """
        Checks for collision with other blocks and the bottom of the grid.
        :return: True if collision. False if not.
        """
        # Checking collision with bottom of the grid.

        for _, y in self.get_grid_positions():
            print(y)


class Square(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "yellow"
        self.shape = np.array([[1, 1, 0],
                               [1, 1, 0],
                               [0, 0, 0]])


class L(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "orange"
        self.shape = np.array([[1, 0, 0],
                               [1, 0, 0],
                               [1, 1, 0]])


class T(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "purple"
        self.shape = np.array([[0, 1, 0],
                               [1, 1, 1],
                               [0, 0, 0]])


class Z(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "green"
        self.shape = np.array([[1, 0, 0],
                               [1, 1, 0],
                               [0, 1, 0]])


class Line(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "blue"
        self.shape = np.array([[0, 1, 0],
                               [0, 1, 0],
                               [0, 1, 0],
                               [0, 1, 0]])


BLOCK_TYPES = [Square, Line, Z, L, T]
