import tkinter


class Display:
    def __init__(self, grid):
        self.grid = grid
        self.window = tkinter.Tk()
        self.window.title("Tetris")
        self.canvas = self.setup_grid_canvas(grid.across, grid.down, 30)
        self.set_up_bindings()

    def set_up_bindings(self):
        def left_handler(event):
            self.grid.current_block.attempt_move_left(self.grid)

        def right_handler(event):
            self.grid.current_block.attempt_move_right(self.grid)

        self.window.bind("a", left_handler)
        self.window.bind("d", right_handler)

    def setup_grid_canvas(self, grid_across, grid_down, cell_size):
        canvas = tkinter.Canvas(master=self.window, width=grid_across * cell_size, height=grid_down * cell_size,
                                background="black")

        for cell_coords in self.grid.cells.keys():
            cell = self.grid.cells[cell_coords]
            x0 = cell.x_grid_coord * cell_size
            y0 = cell.y_grid_coord * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            cell.display_rectangle = canvas.create_rectangle(x0, y0, x1, y1,
                                                             outline=cell.outline_colour,
                                                             fill=cell.empty_colour)

        canvas.pack()

        return canvas

    def clear_cell_colours(self):
        for cell in self.grid.cells.values():
            self.canvas.itemconfig(cell.display_rectangle, fill=cell.empty_colour)

    def update_cells(self):
        self.clear_cell_colours()

        for cell in self.grid.cells.values():
            self.canvas.itemconfig(cell.display_rectangle, fill=cell.colour)

    def start(self):
        self.window.mainloop()
