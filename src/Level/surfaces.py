"""Level.surfaces.py

Module containing surface functionality.
"""

from typing import Tuple

import pygame

from ..Internal import check_type


class Surface(pygame.Rect):
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
        """

        # type checks
        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(width, int, float)
        check_type(height, int, float)
        check_type(has_collision, bool)

        super().__init__(xcor, ycor, width, height)

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.width: int | float = width
        self.height: int | float = height

        self.top: int | float = self.ycor
        self.bottom: int | float = self.ycor + self.height
        self.left: int | float = self.xcor
        self.right: int | float = self.xcor + self.width

        self.has_collision: bool = has_collision
        self.color: Tuple[int, int, int] = color

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
