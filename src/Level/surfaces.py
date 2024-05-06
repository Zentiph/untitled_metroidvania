"""Level.surfaces.py

Module containing surface functionality.
"""

from typing import Tuple

import pygame

from ..Internal import check_type


class Surface:
    """Base class for all surface objects.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        floor_collision: bool = False,
        left_wall_collision: bool = False,
        right_wall_collision: bool = False,
        ceiling_collision: bool = False
    ) -> None:
        """Initializer for all surface objects.

        :param x: The x position of the surface.
        :type x: int | float
        :param y: The y position of the surface.
        :type y: int | float
        :param width: The width of the surface.
        :type width: int | float
        :param height: The height of the surface.
        :type height: int | float
        :param floor_collision: Whether the surface will have floor collision.
        :type floor_collision: bool, optional
        :param left_wall_collision: Whether the surface will have left wall collision.
        :type left_wall_collision: bool, optional
        :param right_wall_collision: Whether the surface will have right wall collision.
        :type right_wall_collision: bool, optional
        :param ceiling_collision: Whether the surface will have ceiling collision.
        :type ceiling_collision: bool, optional
        """

        # type checks
        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(width, int, float)
        check_type(height, int, float)

        check_type(floor_collision, bool)
        check_type(left_wall_collision, bool)
        check_type(right_wall_collision, bool)
        check_type(ceiling_collision, bool)

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.width: int | float = width
        self.height: int | float = height

        self.floor_collision: bool = floor_collision
        self.left_wall_collision: bool = left_wall_collision
        self.right_wall_collision: bool = right_wall_collision
        self.ceiling_collision: bool = ceiling_collision

        self.color: Tuple[int] = (0, 0, 255)

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
            (self.xcor, self.ycor, self.width, self.height)
        )
