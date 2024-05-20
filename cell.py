class Cell:
    def __init__(self, x_grid_coord, y_grid_coord):
        self.x_grid_coord = x_grid_coord
        self.y_grid_coord = y_grid_coord
        self.colour = "skyBlue3"
        self.outline_colour = "black"
        self.display_rectangle = None

    def change_colour(self, colour, canvas):
        self.colour = colour
        canvas.itemconfig(self.display_rectangle, fill=colour)
