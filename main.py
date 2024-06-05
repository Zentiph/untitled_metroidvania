"""main.py

The main module of the project. Runs the gameloop.
"""

import os
from typing import Tuple

import pygame
from screeninfo import get_monitors

from src import GUI, Internal, Level, Player, Stages
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

# setup the player to spawn in stage 1
plr: Player.Player = Player.Player(
    200,
    730,
    width=50,
    height=80,
    speed=250,
    health=10,
    max_health=10,
    has_collision=True,
    color=(255, 0, 0),
)

healthbar: GUI.HealthBar = GUI.HealthBar(0, Internal.SCREEN_HEIGHT - 60, plr)

screen_objects: Tuple[
    Tuple[
        int,
        int,
    ],
    Level.Group,
    Level.Group | None,
    Level.Group | None,
    Tuple[Stages.TextInfo, ...] | None,
] = Stages.STAGES[1]

jump_debounce: bool = False
dash_debounce: bool = False

# the stage the player was in last frame
previous_stage: int | str = plr.stage


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
        if plr.facing_right:
            plr.moveto(plr.xcor + 150, plr.ycor, 0.2, interp.ease_out_circ, False)
        if plr.facing_left:
            plr.moveto(plr.xcor - 150, plr.ycor, 0.2, interp.ease_out_circ, False)
        start_time_i = pygame.time.get_ticks()
        dash_debounce = True

    # restart if died
    if keys[pygame.K_r] and plr.stage == "GAME_OVER":
        plr.xcor, plr.ycor = (200, 730)
        plr.grid_xcor, plr.grid_ycor = (1, 1)
        plr.health = 10

    # DEBUG ROOM KEYBIND
    if keys[pygame.K_LCTRL] and keys[pygame.K_d] and plr.stage != "DEBUG":
        plr.xcor = 200
        plr.ycor = Internal.SCREEN_HEIGHT - plr.height - 100
        plr.grid_xcor, plr.grid_ycor = (-1, -1)

    # exit debug room
    if keys[pygame.K_LCTRL] and keys[pygame.K_a] and plr.stage == "DEBUG":
        plr.xcor = 200
        plr.ycor = Internal.SCREEN_HEIGHT - plr.height - 100
        plr.grid_xcor, plr.grid_ycor = (1, 1)

    # exit game
    # maybe we'll add a menu later
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    # run any update logic for the player
    plr.update_(dt, screen_objects)

    # update the stage objects if the player changes screens
    if previous_stage != plr.stage:
        screen_objects = Stages.STAGES[plr.stage]

    # redraw the updated items on the screen
    screen.fill((0, 0, 0))

    plr.draw(screen)

    screen_objects[1].draw(screen)

    # draw the objects if they are not None
    if screen_objects[2]:
        screen_objects[2].draw(screen)
    if screen_objects[3]:
        screen_objects[3].draw(screen)

    stage_text = screen_objects[4]
    if stage_text:
        for text in stage_text:
            screen.blit(
                pygame.font.SysFont("8514oem", text.size).render(
                    text.msg, False, text.color
                ),
                (text.xcor + 50, text.ycor),
            )

    if jump_debounce and pygame.time.get_ticks() - start_time_j >= 400:
        jump_debounce = False

    if (
        dash_debounce
        and pygame.time.get_ticks() - start_time_i >= 400
        and plr.on_ground
    ):
        dash_debounce = False

    # the healthbar is updated last so it is drawn on top of everything
    healthbar.update(screen)

    # update frame by frame data
    previous_stage = plr.stage
    plr.i_frames -= 1 if plr.i_frames > 0 else 0

    pygame.display.flip()
