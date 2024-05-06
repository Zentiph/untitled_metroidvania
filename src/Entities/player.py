"""player.py

Module containing player related functionality.
"""

from typing import List, Tuple

import pygame
from ..Internal import check_type, GRAVITY_ACCELERATION
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

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.width: int | float = 50
        self.height: int | float = 50

        self.speed: int | float = 250
        self.x_vel: int | float = 0
        self.y_vel: int | float = 0
        self.on_ground: bool = False

        self.color: Tuple[int] = (255, 0, 0)

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

    def jump(
        self,
        dt: int | float
    ) -> None:
        """Increases the player's vertical velocity.

        :param dt: Delta time.
        :type dt: int | float
        """

        if self.on_ground:
            self.y_vel -= 500
            self.on_ground = False

    def check_collision(
        self,
        platforms: List[Surface]
    ) -> None:
        """Run checks on the Player's collisions with other objects.

        :param surfaces: A list of surfaces necessary for collision checks.
        :type surfaces: List[Surface]
        :param x_vel: The x velocity of the player.
        :type x_vel: int | float
        :param y_vel: The y velocity of the player.
        :type y_vel: int | float
        """

        check_type(platforms, list)

        for platform in platforms:
            check_type(platform, Surface)

            # left walls
            if platform.left_wall_collision:
                if self.xcor + self.width > platform.xcor \
                        and self.xcor < platform.xcor:
                    if (self.ycor + self.height > platform.ycor + 5) \
                            and (self.ycor < platform.ycor + platform.height - 5):

                        self.xcor = platform.xcor - self.width

            # floors
            if platform.floor_collision:
                if self.ycor + self.height > platform.ycor - 1 \
                        and self.ycor < platform.ycor + platform.height + 1:
                    if (self.xcor + self.width > platform.xcor) \
                            and (self.xcor < platform.xcor + platform.width):

                        self.ycor = platform.ycor - self.height
                        self.y_vel = 0
                        self.on_ground = True

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

        self.check_collision(platforms)

        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

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
