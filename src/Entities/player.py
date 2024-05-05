"""player.py

Module containing player related functionality.
"""

from typing import List

import pygame
from ..Internal import check_type, GRAVITY
from ..Level import Surface


class Player:
    """A class representing the player object.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float
    ) -> None:
        """Initializer for the player object.

        :param xcor: The x position of the player object.
        :type xcor: int
        :param ycor: The y position of the player object.
        :type ycor: int
        """

        # type checking
        check_type(xcor, int, float)
        check_type(ycor, int, float)

        self.xcor = xcor
        self.ycor = ycor
        self.width = 50
        self.height = 50

        self.speed = 250
        self.vertical_velocity = 0
        self.on_ground = False

        self.color = (255, 0, 0)

    def move_left(
        self,
        dt: int | float
    ) -> None:
        """Moves the player left.

        :param dt: Delta time.
        :type dt: int | float
        """

        check_type(dt, int, float)
        self.xcor -= self.speed * dt

    def move_right(
        self,
        dt: int | float
    ) -> None:
        """Moves the player right.

        :param dt: Delta time.
        :type dt: int | float
        """

        check_type(dt, int, float)
        self.xcor += self.speed * dt

    def jump(self) -> None:
        """Increases the player's vertical velocity.

        :param dt: Delta time.
        :type dt: int | float
        """

        if self.on_ground:
            self.vertical_velocity -= 500

    def update(
        self,
        dt: int | float,
        platforms: List[Surface]
    ) -> None:
        """Runs update checks on the player.

        :param dt: Delta time.
        :type dt: int | float
        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: List[Surface]
        """

        check_type(dt, int, float)
        check_type(platforms, list)
        for platform in platforms:
            check_type(platform, Surface)

        self.vertical_velocity += GRAVITY * dt
        self.ycor += self.vertical_velocity * dt
        self.on_ground = False

        # floor collision
        for platform in platforms:
            if self.ycor < platform.ycor and self.ycor > platform.ycor - platform.height:
                if (self.xcor + self.width > platform.xcor) \
                        and (self.xcor < platform.xcor + platform.width):

                    self.ycor = platform.ycor - platform.height
                    self.vertical_velocity = 0
                    self.on_ground = True

    def draw(
        self,
        screen: pygame.Surface
    ) -> None:
        """Draws the player to the screen.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)

        pygame.draw.rect(
            screen,
            self.color,
            (self.xcor, self.ycor, self.width, self.height)
        )
