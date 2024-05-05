"""main.py

The main module of the project. Runs the gameloop.
"""

import pygame

from src import Entities
from src import Internal
from src import Level

pygame.init()

screen = pygame.display.set_mode((800, 600))

plr = Entities.Player(50, 0)
platforms = [
    Level.Surface(0, 500, 200, 50, is_floor=True),
    Level.Surface(200, 400, 200, 100, is_floor=True),
    Level.Surface(600, 200, 200, 10, is_floor=True),
]

while True:
    # limits the game to 60fps and gets the time delta
    dt = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        plr.move_left(dt)
    if keys[pygame.K_d]:
        plr.move_right(dt)
    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
        plr.jump()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    plr.update(dt, platforms)

    screen.fill((255, 255, 255))
    plr.draw(screen)
    for platform in platforms:
        platform.draw(screen)
    pygame.display.flip()
