"""Level.surfaces.py

Module containing surface functionality.
"""

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
        is_floor: bool = False,
        is_left_wall: bool = False,
        is_right_wall: bool = False,
        is_ceiling: bool = False
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
        :param is_floor: Whether the surface will have floor collision.
        :type is_floor: bool, optional
        :param is_left_wall: Whether the surface will have left wall collision.
        :type is_left_wall: bool, optional
        :param is_right_wall: Whether the surface will have right wall collision.
        :type is_right_wall: bool, optional
        :param is_ceiling: Whether the surface will have ceiling collision.
        :type is_ceiling: bool, optional
        """

        # type checks
        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(width, int, float)
        check_type(height, int, float)

        check_type(is_floor, bool)
        check_type(is_left_wall, bool)
        check_type(is_right_wall, bool)
        check_type(is_ceiling, bool)

        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.height = height

        self.is_floor = is_floor
        self.is_left_wall = is_left_wall
        self.is_right_wall = is_right_wall
        self.is_ceiling = is_ceiling

        self.color = (0, 0, 255)

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
