# This is going to create the map

# Possible algorithms:
# noise map
# random
# fractal
# wave function colapse algorithm

import parameters
import random

class Map:
    def __init__(self):
        # Create the empty map
        self.grid = [[0 for _ in range(parameters.columns)] for _ in range(parameters.rows)]

        for i in self.grid:
            print(i)

    def algoridm(self):
        # Here goes the algorithm
        pass

    def update(self):
        # Update the map every frame (it does some random things to test)
        self.grid[random.randrange(0, 10)][random.randrange(0, 10)] = random.randrange(0, 2)
        pass


if  __name__ == "__main__":
    my_map = Map()