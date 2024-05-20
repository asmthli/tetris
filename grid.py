from block import Block


class Grid:
    def __init__(self, across, down):
        self.across = across
        self.down = down
        self.blocks = self.create()

    def create(self):
        blocks = {}
        for x in range(self.across):
            for y in range(self.down):
                blocks[(x, y)] = Block(x, y)

        return blocks



