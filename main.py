"""main.py

The main module of the project. Runs the gameloop.
"""

import os
from typing import List

import pygame

from screeninfo import get_monitors
from src import Entities, Internal, Level


# get the main monitor info,
# then set the pygame window to open in the center of the screen
MONITOR = get_monitors()[0]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_X: int = MONITOR.width / 2 - SCREEN_WIDTH / 2
WINDOW_Y: int = MONITOR.height / 2 - SCREEN_HEIGHT / 2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_X, WINDOW_Y)
pygame.init()

screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Untitled Metroidvania.")

# set the player and collision platforms
plr: Entities.Player = Entities.Player(
    50,
    0,
    50,
    80,
    250,
    10,
    10,
    (255, 0, 0)
)
collision_platforms: List[Level.Surface] = [
    Level.Surface(0, 500, 800, 50, True),
    Level.Surface(400, 400, 200, 200, True),
    Level.Surface(0, 300, 200, 50, True)
]

# anything inside while True is the gameloop
# this code executes each frame
while True:
    # limits the game to 60fps and gets the time delta
    dt: float = pygame.time.Clock().tick_busy_loop(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # what to do if certain keys are pressed
    keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        plr.move_left(dt)
    if keys[pygame.K_d]:
        plr.move_right(dt)
    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
        plr.jump()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # run any update logic for the player
    plr.update(dt, collision_platforms)

    # redraw the updated items on the screen
    screen.fill((0, 0, 0))
    plr.draw(screen)
    for platform in collision_platforms:
        platform.draw(screen)
    pygame.display.flip()
