class Cell:
    def __init__(self, x_grid_coord, y_grid_coord):
        self.x_grid_coord = x_grid_coord
        self.y_grid_coord = y_grid_coord
        self.empty_colour = "skyBlue3"
        self.active_colour = self.empty_colour
        self.outline_colour = "black"
        self.display_rectangle = None
        self.active = False

    def get_colour(self):
        if self.active:
            return self.active_colour
        else:
            return self.empty_colour
