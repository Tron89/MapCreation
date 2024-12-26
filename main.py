# This will be the main for a map creator

import pygame
from pygame.sprite import Sprite
import parameters
from map import Map
from grid import Grid

Map = Map()
Grid = Grid()

# Create the window
width, heigth = parameters.width, parameters.heigth
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()

while True:
    clock.tick(60) # fps at it will go

    frame_rate = str(int(clock.get_fps()))
    pygame.display.set_caption(parameters.caption + " - FPS:" + frame_rate)

    # --- EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # --- /EVENTS

    # --- LOGIC

    Map.update()

    Grid.update(Map)

    # --- /LOGIC

    screen.fill((255, 255, 255)) 

    # --- SCREEN

    Grid.draw(screen)

    # --- /SCREEN

    pygame.display.flip()
    clock.tick()

pygame.quit()


