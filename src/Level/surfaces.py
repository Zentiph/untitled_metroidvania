"""Level.surfaces.py

Module containing surface functionality.
"""

from typing import Tuple

import pygame

from ..Internal import check_type, Hitbox


class Surface(Hitbox):
    """Class used to create surface objects.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        has_collision: bool = True,
        color: Tuple[int, int, int] = (0, 0, 255)
    ) -> None:
        """Initializer for Surface objects.

        :param x: The x position of the surface.
        :type x: int | float
        :param y: The y position of the surface.
        :type y: int | float
        :param width: The width of the surface.
        :type width: int | float
        :param height: The height of the surface.
        :type height: int | float
        :param has_collision: Whether the surface has collision.
        :type has_collision: bool, optional
        :param color: The color of the surface.
        :type color: Tuple[int], optional
        """

        super().__init__(xcor, ycor, width, height, has_collision, color)

    def draw(
        self,
        screen: pygame.Surface
    ) -> None:
        """Draws the surface to the screen.

        :param screen: The screen to draw the surface.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)
        pygame.draw.rect(
            screen,
            self.color,
            (self.left, self.top, self.width, self.height)
        )


class Spike(Hitbox):
    """Class used to create Spike objects.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        color: Tuple[int, int, int] = (255, 128, 0)
    ) -> None:
        """Initializer for Spike objects.

        :param x: The x position of the spike.
        :type x: int | float
        :param y: The y position of the spike.
        :type y: int | float
        :param width: The width of the spike.
        :type width: int | float
        :param height: The height of the spike.
        :type height: int | float
        :param color: The color of the spike.
        :type color: Tuple[int], optional
        """

        super().__init__(xcor, ycor, width, height, color)

    def draw(
        self,
        screen: pygame.Surface
    ) -> None:
        """Draws the spike to the screen.

        :param screen: The screen to draw the spike.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)
        # TODO
        pygame.draw.polygon(
            screen,
            self.color,
            (self.coords.bottom_left(),
             (self.coords.center_x, self.coords.top()),
             self.coords.bottom_right())
        )
