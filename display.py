import tkinter
import tkinter.font
from utils import average_run_timer


class Display:
    def __init__(self, grid, grid_cell_size):
        self.grid = grid
        self.window = tkinter.Tk()
        self.window.title("Tetris")
        self.canvas_height = grid.down * grid_cell_size
        self.canvas_width = grid.across * grid_cell_size
        self.canvas = self.setup_grid_canvas(grid_cell_size)
        self.score_text = self.setup_score()

        self.down_pressed = False
        self.set_up_bindings()

    def set_up_bindings(self):
        def left_handler(event):
            self.grid.current_block.attempt_move_left(self.grid)

        def right_handler(event):
            self.grid.current_block.attempt_move_right(self.grid)

        def rotation_handler(event):
            self.grid.current_block.attempt_rotation(self.grid)

        def down_press_handler(event):
            self.down_pressed = True

        def down_release_handler(event):
            self.down_pressed = False

        self.window.bind("a", left_handler)
        self.window.bind("d", right_handler)
        self.window.bind("w", rotation_handler)
        self.window.bind("<KeyPress-s>", down_press_handler)
        self.window.bind("<KeyRelease-s>", down_release_handler)

    def setup_grid_canvas(self, grid_cell_size):
        canvas = tkinter.Canvas(master=self.window, width=self.canvas_width, height=self.canvas_height,
                                background="black")

        for cell_coords in self.grid.cells.keys():
            cell = self.grid.cells[cell_coords]
            x0 = cell.x_grid_coord * grid_cell_size
            y0 = cell.y_grid_coord * grid_cell_size
            x1 = x0 + grid_cell_size
            y1 = y0 + grid_cell_size
            cell.display_rectangle = canvas.create_rectangle(x0, y0, x1, y1,
                                                             outline=cell.outline_colour,
                                                             fill=cell.empty_colour)

        canvas.pack()

        return canvas

    def setup_score(self):
        score_text = tkinter.Text()

        return score_text

    @average_run_timer
    def update_cells(self):
        for cell in self.grid.cells.values():
            self.canvas.itemconfig(cell.display_rectangle, fill=cell.get_colour())

    def show_game_over(self, final_score):
        font = tkinter.font.Font(family="Comic Sans MS",
                                 size=20,
                                 weight="bold")

        self.canvas.create_text(self.canvas_width / 2,
                                self.canvas_height / 2,
                                text=f"Game over!\nScore: {final_score}",
                                font=font,
                                fill="maroon",
                                justify="center")

    def start(self):
        self.window.mainloop()
