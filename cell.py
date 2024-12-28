import pygame
from pygame.sprite import Sprite
import parameters

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, default_img = None):
        super().__init__()
        self.image = default_img if default_img else pygame.Surface((parameters.cell_width, parameters.cell_height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def setImage(self, img):
        self.image = img
    
    def setColor(self, color):
        self.image.fill(color)