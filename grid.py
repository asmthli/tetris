from cell import Cell
from block import BLOCK_TYPES
import random


class Grid:
    def __init__(self, across, down):
        self.across = across
        self.down = down
        self.cells = self.create()
        self.active_cells = []
        self.current_block = None

    def generate_new_block(self):
        x_offset = random.randint(0, self.across - 1 - 3)
        block = random.choice(BLOCK_TYPES)(x_offset)

        self.current_block = block

    def mark_cells_active(self):
        """
        To be used when a block comes to a stop. Cells are marked active for later collision detection etc.
        :return: None
        """
        for x, y in self.current_block.block_cell_positions:
            active_cell = self.cells[(x, y)]
            self.active_cells.append(active_cell)

    def check_for_complete_rows(self):
        for y in range(self.down - 1, -1, -1):
            for x in range(0, self.across):
                if not self.cells[(x, y)].active:
                    break

                if x == self.across - 1:
                    # Row is complete.
                    return y
        return None

    def update_cell_colours(self):
        """
        Updates the grid cell colours for each of the active blocks.
        This should be called whenever a block has moved - i.e. once every game tick.

        Note that the actual redrawing of cells is done in the display module.
        :return: None
        """
        for cell in self.cells.values():
            cell.active = False

        for cell in self.active_cells:
            cell.active = True

        for x, y in self.current_block.block_cell_positions:
            cell = self.cells[(x, y)]
            cell.active = True
            cell.active_colour = self.current_block.colour

    def create(self):
        cells = {}
        for x in range(self.across):
            for y in range(self.down):
                cells[(x, y)] = Cell(x, y)

        return cells
