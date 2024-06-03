"""main.py

The main module of the project. Runs the gameloop.
"""

import os

import pygame

from screeninfo import get_monitors
from src import Entities, GUI, Internal, Level
from src.Internal import interp


# get the main monitor info,
# then set the pygame window to open in the center of the screen
MONITOR = get_monitors()[0]
WINDOW_X: int = MONITOR.width // 2 - Internal.SCREEN_WIDTH // 2
WINDOW_Y: int = MONITOR.height // 2 - Internal.SCREEN_HEIGHT // 2
os.environ["SDL_VIDEO_WINDOW_POS"] = f"{WINDOW_X}, {WINDOW_Y}"
pygame.init()

screen: pygame.Surface = pygame.display.set_mode(
    (Internal.SCREEN_WIDTH, Internal.SCREEN_HEIGHT)
)
pygame.display.set_caption("Untitled Metroidvania.")

# set the player and collision platforms
plr: Entities.Player = Entities.Player(
    50,
    0,
    width=50,
    height=80,
    speed=250,
    health=10,
    max_health=10,
    has_collision=True,
    color=(255, 0, 0),
)
healthbar: GUI.HealthBar = GUI.HealthBar(0, Internal.SCREEN_HEIGHT - 30, plr)

platforms: Level.Group = Level.Group(
    Level.Platform(0, 500, 1400, 50, True),
    Level.Platform(400, 400, 120, 200, True),
    Level.Platform(0, 300, 200, 50, True),
)

spikes: Level.Group = Level.Group(
    Level.Spike(800, 450, 50, 50),
    Level.Spike(850, 450, 50, 50),
    Level.Spike(900, 450, 50, 50),
    Level.Spike(950, 450, 50, 50),
    Level.Spike(1000, 450, 50, 50),
)

screen_objects: Level.Group = Level.Group(platforms)

jump_debounce: bool = False
dash_debounce: bool = False

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

    # walking
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        plr.move_left(dt)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        plr.move_right(dt)

    # jumping
    if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        if plr.on_ground:
            plr.jump()
            start_time_j = pygame.time.get_ticks()
            jump_debounce = True
        elif not jump_debounce and not plr.double_jump_debounce:
            plr.double_jump()

    # dashing
    if keys[pygame.K_LSHIFT] and not dash_debounce:
        if plr.face_rt:
            plr.moveto(plr.xcor + 250, plr.ycor, 0.2, interp.ease_out_circ, False)
        if plr.face_lf:
            plr.moveto(plr.xcor - 250, plr.ycor, 0.2, interp.ease_out_circ, False)
        start_time_i = pygame.time.get_ticks()
        dash_debounce = True

    # exit game
    # maybe we'll add a menu later
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # run any update logic for the player
    plr.update_(dt, platforms)

    # redraw the updated items on the screen
    screen.fill((0, 0, 0))

    plr.draw(screen)
    healthbar.update(screen)

    platforms.draw(screen)
    spikes.draw(screen)

    if jump_debounce and pygame.time.get_ticks() - start_time_j >= 400:
        jump_debounce = False

    if (
        dash_debounce
        and pygame.time.get_ticks() - start_time_i >= 400
        and plr.on_ground
    ):
        dash_debounce = False

    pygame.display.flip()
