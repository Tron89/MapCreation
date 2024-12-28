# This is going to create the map

# Possible algorithms:
# noise map
# random
# fractal
# wave function colapse algorithm

import parameters
from algorithms.random_algorithm import RandomAlgorithm
from algorithms.wfc_algorithm import WFCAlgorithm


class Map:
    finish = False

    def __init__(self):
        # Create the empty map
        self.grid = [[0 for _ in range(parameters.columns)] for _ in range(parameters.rows)]
        
        self.RandomAlgorithm = RandomAlgorithm(self.grid, loop=True)
        self.WFCAlgorithm = WFCAlgorithm(self.grid)


    def update(self):
        # Update the map every frame (it does some random things to test)
        if parameters.algorithm == "random":
            if self.finish == False:
                if self.RandomAlgorithm.update() == True:
                    self.finish = True
        elif parameters.algorithm == "wfc":
            if self.finish == False:
                self.WFCAlgorithm.update()





if  __name__ == "__main__":
    my_map = Map()