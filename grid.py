from cell import Cell
from block import BLOCK_TYPES, Block
import random


class Grid:
    def __init__(self, across, down):
        self.across = across
        self.down = down
        self.cells = self.create()
        self.active_blocks = []
        self.current_block = None

    def generate_new_block(self):
        x_offset = random.randint(0, self.across-1-3)
        block = random.choice(BLOCK_TYPES)(x_offset)

        self.active_blocks.append(block)
        self.current_block = block

    def update_cell_colours(self):
        """
        Updates the grid cell colours for each of the active blocks.
        This should be called whenever a block has moved - i.e. once every game tick.

        Note that the actual redrawing of cells is done in the display module.
        :return: None
        """
        for cell in self.cells.values():
            cell.reset()

        for block in self.active_blocks:
            block_grid_positions = block.get_grid_positions()
            for position in block_grid_positions:
                self.cells[position].colour = block.colour

    def create(self):
        cells = {}
        for x in range(self.across):
            for y in range(self.down):
                cells[(x, y)] = Cell(x, y)

        return cells
