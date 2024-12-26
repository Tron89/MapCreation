"""
    This is going to create the map
"""

"""
    algoridm potions:
    noise map
    random
    fractal
    wave function colapse algoridm

"""

import parameters


class Map:
    def __init__(self):
        #create the empty map
        self.grid = [[0 for _ in range(parameters.columns)] for _ in range(parameters.rows)]
        print(self.grid)

    def algoridm(self):
        #heare goes the algorithm
        pass

    def update(self):
        pass


if  __name__ == "__main__":
    my_map = Map()