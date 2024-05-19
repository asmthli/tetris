import tkinter


class Display:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Tetris")
        self.window.config(padx=50, pady=50, background="white")
