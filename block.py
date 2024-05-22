import numpy as np


class Block:

    def __init__(self, x_offset):
        self.grid_x_offset = x_offset
        self.grid_y_offset = 0
        self.rotation_offset = 0
        self.shape = None
        self.block_cell_positions = None

    def update_cell_positions(self):
        positions = []
        for y in range(self.shape.shape[0]):
            for x in range(self.shape.shape[1]):
                binary = self.shape[y, x]
                if binary == 1:
                    offset_y = y + self.grid_y_offset
                    offset_x = x + self.grid_x_offset
                    positions.append((offset_x, offset_y))

        return positions

    def attempt_move_down(self, grid):
        can_move = not self.has_bottom_collision(grid) and not self.has_block_collision(grid, "down")
        if can_move:
            self.grid_y_offset += 1
            self.block_cell_positions = self.update_cell_positions()
            return True
        else:
            return False

    def move_up(self):
        self.grid_y_offset -= 1
        self.block_cell_positions = self.update_cell_positions()

    def attempt_move_left(self, grid):
        can_move = not self.has_block_collision(grid, "left") and not self.has_wall_collision(grid, "left")
        if can_move:
            self.grid_x_offset -= 1
            self.block_cell_positions = self.update_cell_positions()
            return True
        else:
            return False

    def attempt_move_right(self, grid):
        can_move = not self.has_block_collision(grid, "right") and not self.has_wall_collision(grid, "right")
        if can_move:
            self.grid_x_offset += 1
            self.block_cell_positions = self.update_cell_positions()
            return True
        else:
            return False

    def undo_movement(self, direction):
        if direction == "down":
            self.grid_y_offset -= 1
        elif direction == "right":
            self.grid_x_offset -= 1
        elif direction == "left":
            self.grid_x_offset += 1
        self.block_cell_positions = self.update_cell_positions()

    def attempt_rotation(self, grid):
        can_rotate = not self.has_wall_collision(grid, "rotation")
        if can_rotate:
            self.shape = np.rot90(self.shape)
            self.block_cell_positions = self.update_cell_positions()

    def has_bottom_collision(self, grid):
        """
        Checks for collision with the bottom of the grid.
        :return: True if collision. False if not.
        """

        # Checking collision with bottom of the grid.
        for _, y in self.block_cell_positions:
            if y >= grid.down - 1:
                return True

        return False

    def has_wall_collision(self, grid, transformation):
        if transformation == "left":
            for x, _ in self.block_cell_positions:
                if x == 0:
                    return True
        elif transformation == "right":
            for x, _ in self.block_cell_positions:
                if x == grid.across - 1:
                    return True
        elif transformation == "rotation":
            self.shape = np.rot90(self.shape)
            potential_cell_positions = self.update_cell_positions()
            for x, _ in potential_cell_positions:
                if x > grid.across - 1:
                    self.shape = np.rot90(self.shape, k=3)
                    return True
            self.shape = np.rot90(self.shape, k=3)

        return False

    def has_block_collision(self, grid, direction):
        """
        Checks for collision with any of the other active blocks.
        :return: True if collision. False if not.
        """
        # We do this by moving the block in the direction of travel for the game tick (always to include down)
        # If this move results in a collision, undo the movement in the direction that caused the collision.
        if direction == "down":
            self.grid_y_offset += 1
        elif direction == "right":
            self.grid_x_offset += 1
        elif direction == "left":
            self.grid_x_offset -= 1
        # TODO: Uncouple the cell positions used in this movement 'testing' from the actual cell positions.
        self.block_cell_positions = self.update_cell_positions()

        for cell in grid.active_cells:
            for block_cell_position in self.block_cell_positions:
                cell_position = (cell.x_grid_coord, cell.y_grid_coord)
                if cell_position == block_cell_position:
                    self.undo_movement(direction)
                    return True
        self.undo_movement(direction)
        return False


class Square(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "yellow"
        self.shape = np.array([[1, 1],
                               [1, 1]])
        self.block_cell_positions = self.update_cell_positions()


class L(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "orange"
        self.shape = np.array([[1, 0],
                               [1, 0],
                               [1, 1]])
        self.block_cell_positions = self.update_cell_positions()


class T(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "purple"
        self.shape = np.array([[0, 1, 0],
                               [1, 1, 1]])
        self.block_cell_positions = self.update_cell_positions()


class Z(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "green"
        self.shape = np.array([[1, 0, 0],
                               [1, 1, 0],
                               [0, 1, 0]])
        self.block_cell_positions = self.update_cell_positions()


class Line(Block):
    def __init__(self, x_offset):
        super().__init__(x_offset)
        self.colour = "blue"
        self.shape = np.array([[1],
                               [1],
                               [1],
                               [1]])
        self.block_cell_positions = self.update_cell_positions()


BLOCK_TYPES = [Square, Line, Z, L, T]
