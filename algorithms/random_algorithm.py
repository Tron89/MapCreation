from grid import Grid
import parameters
import random

class RandomAlgorithm:

    stepx = 0
    stepy = 0

    def __init__(self, grid, loop = False):
        self.grid = grid
        self.loop = loop

    def update(self):
        self.grid[self.stepy][self.stepx] = random.randrange(1, len(Grid.colors))

        self.stepx += 1
        if self.stepx == parameters.columns:
            self.stepx = 0
            self.stepy += 1
            if self.stepy == parameters.rows:
                self.stepy = 0
                if self.loop == False:
                    return True