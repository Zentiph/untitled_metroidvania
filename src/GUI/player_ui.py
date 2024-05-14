"""GUI.player_ui.py

player_ui contains various functions used for the creation
and utilization of graphical aspects that are visible at
all times outside of menus.
"""

from pygame import Rect, draw, display, font
from ..Entities import Player


class HealthBar:
    def __init__(self, screen, xcor, ycor, PlayerCharacter):
        draw.rect(screen, (255, 0, 0), Rect(xcor, ycor, 200, 30))
        draw.rect(screen, (0, 255, 0), Rect(xcor, ycor, 200*(PlayerCharacter.health/PlayerCharacter.max_health), 30))
        screen.blit(font.SysFont("Comic Sans MS", 30).render(f"{round(PlayerCharacter.health)} / {PlayerCharacter.max_health}", False, (0, 0, 0)), (xcor+50, ycor-6))