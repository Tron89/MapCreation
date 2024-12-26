# This handles the grid of the map, and the cells that are going to be displayed on the screen.

import pygame
from pygame.sprite import Sprite
import parameters
from cell import Cell


class Grid:
    
    # Load images
    images = {
        0 : pygame.transform.scale(pygame.image.load('./img/placeholder.jpg'), (parameters.cell_width, parameters.cell_height)),
        1 : pygame.transform.scale(pygame.image.load('./img/car.png'), (parameters.cell_width, parameters.cell_height)),
    }

    def __init__(self):

        # Create the cells
        self.cells_sprites = pygame.sprite.Group()
        self.cells_matrix = [[0 for column in range(parameters.columns)] for row in range(parameters.rows)]

        for row in range(parameters.rows):
            for column in range(parameters.columns):
                # TODO: add border??
                cell = Cell(column * parameters.cell_width, row * parameters.cell_height, self.images[0])
                self.cells_matrix[row][column] = cell
                self.cells_sprites.add(cell)

    def update(self, Map):
        # Use the map grid to update the cells to his images
        for row in range(parameters.rows):
            for column in range(parameters.columns):
                self.cells_matrix[row][column].setImage(self.images[Map.grid[row][column]])

    def draw(self, screen):
        self.cells_sprites.draw(screen)


