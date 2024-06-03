"""GUI.player_ui.py

player_ui contains various functions used for the creation
and utilization of graphical aspects that are visible at
all times outside of menus.
"""

import pygame
from ..Entities import Player


class HealthBar:
    """Class for displaying the player healthbar."""

    def __init__(self, xcor: int | float, ycor: int | float, plr: Player) -> None:
        """Initializer for the HealthBar object.

        :param xcor: The x-coordinate of the HealthBar object.
        :type xcor: int | float
        :param ycor: The y-coordinate of the HealthBar object.
        :type ycor: int | float
        :param plr: The Player object to which the HealthBar object belongs.
        :type plr: Player
        """

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.plr: Player = plr

    def update(self, screen: pygame.Surface) -> None:
        """Runs update checks on the HealthBar.

        :param screen: _description_
        :type screen: pygame.Surface
        """

        pygame.draw.rect(
            screen, (255, 0, 0), pygame.Rect(self.xcor, self.ycor, 200, 30)
        )
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            pygame.Rect(
                self.xcor, self.ycor, 200 * (self.plr.health / self.plr.max_health), 30
            ),
        )
        screen.blit(
            pygame.font.SysFont("8514oem", 45).render(
                f"{round(self.plr.health)} / {self.plr.max_health}", False, (0, 0, 0)
            ),
            (self.xcor + 50, self.ycor),
        )
