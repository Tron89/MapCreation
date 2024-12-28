# This handles the grid of the map, and the cells that are going to be displayed on the screen.

import pygame
from pygame.sprite import Sprite
import parameters
from cell import Cell

# Cells (for the wave function colapse algorithm)
# 1 - See (blue)
# 2 - Sand (yellow)
# 3 - Field (light green)
# 4 - Forest (green)
# 5 - Mountain (brown)


class Grid:
    
    # If someday I want to use images instead of colors
    # Load images
    # images = {
    #     0 : pygame.transform.scale(pygame.image.load('./img/placeholder.jpg'), (parameters.cell_width, parameters.cell_height)),
    #     1 : pygame.transform.scale(pygame.image.load('./img/car.png'), (parameters.cell_width, parameters.cell_height)),
    #     2 : pygame.transform.scale(pygame.image.load('./img/car.png'), (parameters.cell_width, parameters.cell_height)),
    # }

    # Set colors 
    colors = {
        0 : (0, 0, 0, 255),
        1 : (0, 0, 255),
        2 : (255, 255, 0),
        3 : (0, 255, 0),
        4 : (0, 150, 0),
        5 : (150, 75, 0),
    }

    def __init__(self):

        # Create the cells
        self.cells_sprites = pygame.sprite.Group()
        self.cells_matrix = [[0 for column in range(parameters.columns)] for row in range(parameters.rows)]

        for row in range(parameters.rows):
            for column in range(parameters.columns):
                # TODO: add border??
                cell = Cell(column * parameters.cell_width, row * parameters.cell_height)
                self.cells_matrix[row][column] = cell
                self.cells_sprites.add(cell)

    def update(self, Map):
        # Use the map grid to update the cells to his images
        for row in range(parameters.rows):
            for column in range(parameters.columns):
                # If someday I want to use images instead of colors
                # self.cells_matrix[row][column].setImage(self.images[Map.grid[row][column]])
                self.cells_matrix[row][column].setColor(self.colors[Map.grid[row][column]])

    def draw(self, screen):
        self.cells_sprites.draw(screen)


