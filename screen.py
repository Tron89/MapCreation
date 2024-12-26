"""
    This is going to display in screen the map in grids
    I going to use pygame
"""
import pygame
import parameters


class Screen:
    def __init__(self):
        #create the empty map
        self.grid = [[0 for _ in range(parameters.columns)] for _ in range(parameters.rows)]
        print(self.grid)


    def update(self, screen):
        self.grid = self.grid
        pass


if  __name__ == "__main__":
    my_map = Map()