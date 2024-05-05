"""main.py

The main module of the project. Runs the gameloop.
"""

import pygame

import src.Entities as Entities
import src.Internal as Internal
import src.Level as Level

pygame.init()

screen = pygame.display.set_mode((800, 600))

plr = Entities.Player(50, 300)
platforms = [
    Level.Surface(0, 500, 200, 50, True, True, True, True),
    Level.Surface(200, 400, 200, 50, True, True, True, True),
    Level.Surface(600, 200, 200, 50, True, True, True, True),
]

while True:
    # limits the game to 60fps and gets the time delta
    dt = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

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

pygame.quit()
