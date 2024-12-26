import pygame
from pygame.sprite import Sprite
import parameters

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, default_img):
        super().__init__()
        self.image = default_img
        self.rect = self.image.get_rect(topleft=(x, y))

    def setImage(self, img):
        self.image = img