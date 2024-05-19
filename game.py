from display import Display


class Game:
    def __init__(self):
        self.display = Display()
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
        print("Test")
        self.set_game_loop()

    def run(self):
        self.set_game_loop()
        self.display.start()


if __name__ == "__main__":
    Game().run()
