from cell import Cell
from block import BLOCK_TYPES
import random


class Grid:
    def __init__(self, across, down):
        self.across = across
        self.down = down
        self.cells = self.create()
        self.blocks = []

    def generate_block(self):
        block = random.choice(BLOCK_TYPES)
        self.blocks.append(block())

    def create(self):
        cells = {}
        for x in range(self.across):
            for y in range(self.down):
                cells[(x, y)] = Cell(x, y)

        return cells
