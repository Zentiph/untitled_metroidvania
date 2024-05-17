"""GUI.player_ui.py

player_ui contains various functions used for the creation
and utilization of graphical aspects that are visible at
all times outside of menus.
"""

<<<<<<< HEAD
from pygame import Rect, draw, display, font
=======
import pygame
>>>>>>> 7a0d21fa72ede961c5998d78d1dd688839626193
from ..Entities import Player


class HealthBar:
<<<<<<< HEAD
    def __init__(self, screen, xcor, ycor, PlayerCharacter):
        draw.rect(screen, (255, 0, 0), Rect(xcor, ycor, 200, 30))
        draw.rect(screen, (0, 255, 0), Rect(xcor, ycor, 200*(PlayerCharacter.health/PlayerCharacter.max_health), 30))
        screen.blit(font.SysFont("Comic Sans MS", 30).render(f"{round(PlayerCharacter.health)} / {PlayerCharacter.max_health}", False, (0, 0, 0)), (xcor+50, ycor-6))
=======
    """Class for displaying the player healthbar.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        plr: Player
    ) -> None:
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

    def update(
        self,
        screen: pygame.Surface
    ) -> None:
        """Runs update checks on the HealthBar.

        :param screen: _description_
        :type screen: pygame.Surface
        """

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(self.xcor, self.ycor, 200, 30)
        )
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            pygame.Rect(
                self.xcor,
                self.ycor,
                200 * (self.plr.health / self.plr.max_health),
                30
            )
        )
        screen.blit(
            pygame.font.SysFont("Comic Sans MS", 30).render(
                f"{round(self.plr.health)} / {self.plr.max_health}",
                False,
                (0, 0, 0)),
            (self.xcor + 50, self.ycor - 6)
        )
>>>>>>> 7a0d21fa72ede961c5998d78d1dd688839626193
