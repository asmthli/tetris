from display import Display
from grid import Grid


class Game:
    def __init__(self, grid_across=10, grid_down=20):
        self.grid = Grid(grid_across, grid_down)
        self.game_tick_time = 200  # ms
        self.display = Display(self.grid, 30)
        self.game_loop_id = None
        self.score = 0

        self.grid.generate_new_block()

    def set_game_loop(self):
        """
        Sets up the game loop to trigger after the given game tick time.

        This should be called to initiate the game loop and then called recursively from the game loop to set a new
        game loop event after the given time.
        :return:
        """
        if self.display.down_pressed:
            self.game_tick_time = 20
        else:
            self.game_tick_time = 200

        self.game_loop_id = self.display.window.after(self.game_tick_time, self.game_loop)

    def game_loop(self):
        self.grid.update_cell_colours()
        self.display.update_cells()

        game_over = False
        move_successful = self.grid.current_block.attempt_move_down(self.grid)
        if not move_successful:
            self.grid.mark_cells_active()
            rows_deleted_count = self.grid.delete_complete_rows()
            self.change_score(rows_deleted_count)
            game_over = self.grid.generate_new_block()

        if game_over:
            self.game_over()
        else:
            self.set_game_loop()

    def change_score(self, rows_deleted_count):
        if rows_deleted_count == 1:
            multiplier = 100
        elif rows_deleted_count == 2:
            multiplier = 300
        elif rows_deleted_count == 3:
            multiplier = 600
        else:
            multiplier = 1000

        self.score += rows_deleted_count*multiplier

    def run(self):
        self.set_game_loop()
        self.display.start()

    def game_over(self):
        self.display.window.after_cancel(self.game_loop_id)
        self.display.show_game_over(self.score)


if __name__ == "__main__":
    Game().run()
