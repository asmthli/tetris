import tkinter


class Display:
    def __init__(self, grid):
        self.grid = grid
        self.window = tkinter.Tk()
        self.window.title("Tetris")
        self.canvas = self.setup_grid_canvas(grid.across, grid.down, 30)

    def setup_grid_canvas(self, grid_across, grid_down, cell_size):
        canvas = tkinter.Canvas(master=self.window, width=grid_across * cell_size, height=grid_down * cell_size,
                                background="black")

        for block_coords in self.grid.blocks.keys():
            block = self.grid.blocks[block_coords]
            x0 = block.x_grid_coord * cell_size
            y0 = block.y_grid_coord * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            block.display_rectangle = canvas.create_rectangle(x0, y0, x1, y1,
                                                              fill=block.colour)

        canvas.pack()

        return canvas

    def start(self):
        self.window.mainloop()
