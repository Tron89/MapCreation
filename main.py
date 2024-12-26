"""
    This will be the main for a map creator
"""

import pygame
from pygame.sprite import Sprite
import parameters
from map import Map
Map = Map()
from screen import Screen
Screen = Screen()








class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./img/car.png') # Load the player image
        self.rect = self.image.get_rect() # Get the player's rectangle
        self.rect.x = 100 # Set the player's x position
        self.rect.y = 100 # Set the player's y position

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)







width, heigth = parameters.width, parameters.heigth
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()



clock.tick(30) # fps at it will go

while True:

    frame_rate = str(int(clock.get_fps()))
    pygame.display.set_caption(parameters.caption + " - FPS:"+frame_rate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # --- LOGIC

    Map.update()

    # --- LOGIC

    
    screen.fill((255, 255, 255)) 

    # --- SCREEN

    Screen.update(screen)

    all_sprites.draw(screen)

    # --- SCREEN

    pygame.display.flip()
    clock.tick()

pygame.quit()


