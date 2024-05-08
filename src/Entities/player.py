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
        self.height: int | float = 80

        self.speed: int | float = 250
        self.x_vel: int | float = 0
        self.y_vel: int | float = 0
        self.on_ground: bool = False

        self.health: int | float = 5
        self.max_health: int | float = 5

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

    def jump(self) -> None:
        """Increases the player's vertical velocity.
        """

        if self.on_ground:
            self.y_vel -= 500
            self.on_ground = False

    def check_surface_collision(
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

            floor = platform.floor
            ceil = platform.ceiling
            lt_wall = platform.left_wall
            rt_wall = platform.right_wall

            # vertical collisions checks (floor and ceiling)
            if floor and self.xcor + self.width > floor.xcor \
                    and self.xcor < floor.xcor + floor.width:
                if self.ycor + self.height > floor.ycor and self.ycor < floor.ycor:
                    # if more than 1/10 of the player's height is below the floor, let them drop
                    if self.ycor + self.height - floor.ycor < self.height / 10:
                        if self.y_vel > 0:  # if the player is moving downwards
                            self.ycor = floor.ycor - self.height
                            self.y_vel = 0
                            self.on_ground = True

            if ceil and self.xcor + self.width > ceil.xcor and self.xcor < ceil.xcor + ceil.width:
                if self.ycor + self.height > ceil.ycor and self.ycor < ceil.ycor:
                    # if more than 1/10 of the player's height is above the ceiling,
                    # and they are near the edge of the surface, let them go up
                    if abs(self.ycor - ceil.ycor) < self.height / 10 and \
                            (ceil.xcor - self.xcor > 1 or self.xcor + self.width - ceil.xcor + ceil.width > 1):
                        if self.y_vel < 0:  # if the player is moving upwards
                            self.ycor = ceil.ycor
                            self.y_vel = 0

            # horizontal collisions checks (left and right walls)
            if lt_wall and self.ycor + self.height > lt_wall.ycor \
                    and self.ycor < lt_wall.ycor + lt_wall.height:
                if self.xcor + self.width > lt_wall.xcor and self.xcor < lt_wall.xcor:
                    self.xcor = lt_wall.xcor - self.width

            if rt_wall and self.ycor + self.height > rt_wall.ycor \
                    and self.ycor < rt_wall.ycor + rt_wall.height:
                if self.xcor + self.width > rt_wall.xcor and self.xcor < rt_wall.xcor:
                    self.xcor = rt_wall.xcor

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

        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

        self.check_surface_collision(platforms)

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
