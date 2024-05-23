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
        potential_x_offsets = list(range(0, self.across - 1 - 3))
        block_type = random.choice(BLOCK_TYPES)

        while potential_x_offsets:
            x_offset = random.choice(potential_x_offsets)
            potential_x_offsets.remove(x_offset)

            block = block_type(x_offset)

            if block.has_block_collision(self):
                if not potential_x_offsets:
                    # The block cannot be placed - game over.
                    return True
                else:
                    continue
            else:
                self.current_block = block
                return False

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

    def move_down_rows_above(self, y):
        """
        Moves down all rows by one y increment. To be used when a line row is completed.
        :param y: y value for a cleared row. All rows with Y < y will be moved down.
        :return: None
        """

        # Necessary to move cells from the bottom up as we will use information from the cell above.
        self.active_cells.sort(key=lambda cell: cell.y_grid_coord)
        # Found some behaviour of Python loops here. Do not delete elements from a list you are iterating over. The
        # implicit index created is not updated after an element is removed and so elements are skipped!
        # Fixed this by iterating a copy of the original active_cells list.
        for current_cell in self.active_cells[:]:
            if current_cell.y_grid_coord < y:
                cell_underneath = self.cells[(current_cell.x_grid_coord, current_cell.y_grid_coord + 1)]
                cell_underneath.active = True
                current_cell.active = False
                cell_underneath.active_colour = current_cell.active_colour

                self.active_cells.append(cell_underneath)
                self.active_cells.remove(current_cell)

    def delete_complete_rows(self):
        deleted_row_count = 0

        def delete():
            nonlocal deleted_row_count
            y = self.check_for_complete_rows()

            if y is not None:
                deleted_row_count += 1
                for x in range(0, self.across):
                    cell = self.cells[(x, y)]
                    cell.active = False
                    self.active_cells.remove(cell)
                # Dealing with potential multiple complete rows.
                delete()
                self.move_down_rows_above(y)
        delete()

        return deleted_row_count

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
