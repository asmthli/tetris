from display import Display
from grid import Grid


class Game:
    def __init__(self, grid_across=10, grid_down=20):
        self.grid = Grid(grid_across, grid_down)
        self.display = Display(self.grid)
        self.game_tick_time = 1000  # 1000ms

    def set_game_loop(self):
        """
        Sets up the game loop to trigger after the given game tick time.

        This should be called to initiate the game loop and then called recursively from the game loop to set a new
        game loop event after the given time.
        :return:
        """
        self.display.window.after(self.game_tick_time, self.game_loop)

    def game_loop(self):
        self.grid.generate_block()

        self.grid.update_cell_colours()
        self.display.update_cells()



        # for each in self.grid.blocks:
        #     positions = each.get_grid_positions()
        #     for pos in positions:
        #         self.grid.cells[pos].change_colour(each.colour, self.display.canvas)

        for block in self.grid.active_blocks:
            block.move_down()


        self.set_game_loop()

    def run(self):
        self.set_game_loop()
        self.display.start()


if __name__ == "__main__":
    Game().run()
