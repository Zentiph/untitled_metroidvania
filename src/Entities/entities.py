"""Entities/entities.py

Module containing entity related functionality.
"""

from typing import Callable, List, Tuple

import pygame
from ..Internal import check_type, GRAVITY_ACCELERATION
from ..Level import Surface


class Entity:
    """Base class for entity objects.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        speed: int | float,
        health: int,
        max_health: int,
        color: Tuple[int]

    ) -> None:
        """Initializer for the entity object.

        :param xcor: The x position of the entity object.
        :type xcor: int | float
        :param ycor: The y position of the entity object.
        :type ycor: int | float
        :param width: The width of the entity object.
        :type width: int | float
        :param height: The height of the entity object.
        :type height: int | float
        :param speed: The speed of the entity object.
        :type speed: int | float
        :param health: The health of the entity object.
        :type health: int
        :param max_health: The maximum health of the entity object.
        :type max_health: int
        :param color: The color of the entity object.
        :type color: Tuple[int]
        """

        # type checking
        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(width, int, float)
        check_type(height, int, float)
        check_type(speed, int, float)
        check_type(health, int)
        check_type(max_health, int)
        check_type(color, tuple)
        for v in color:
            check_type(v, int)
            if v < 0 or v > 255:
                raise ValueError(f"Color value {v} is out of range.")
        if len(color) != 3:
            raise ValueError(
                f"Color tuple must be of length 3, not {len(color)}."
            )

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.width: int | float = width
        self.height: int | float = height

        self.speed: int | float = speed
        self.y_vel: int | float = 0
        self.on_ground: bool = False

        self.health: int | float = health
        self.max_health: int | float = max_health

        self.color: Tuple[int] = color

    def move_left(
        self,
        dt: int | float
    ) -> None:
        """Moves the entity left.

        :param dt: Delta time.
        :type dt: int | float
        """

        check_type(dt, int, float)
        self.xcor -= self.speed * dt

    def move_right(
        self,
        dt: int | float
    ) -> None:
        """Moves the entity right.

        :param dt: Delta time.
        :type dt: int | float
        """

        check_type(dt, int, float)
        self.xcor += self.speed * dt

    def jump(self) -> None:
        """Increases the entity's vertical velocity.
        """

        if self.on_ground:
            self.y_vel -= 500
            self.on_ground = False

    def check_surface_collision(
        self,
        platforms: List[Surface]
    ) -> None:
        """Run checks on the entity's collisions with other objects.

        :param surfaces: A list of surfaces necessary for collision checks.
        :type surfaces: List[Surface]
        :param x_vel: The x velocity of the entity.
        :type x_vel: int | float
        :param y_vel: The y velocity of the entity.
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
                    # if more than 1/10 of the entity's height is below the floor, let them drop
                    if self.ycor + self.height - floor.ycor < self.height / 10:
                        if self.y_vel > 0:  # if the entity is moving downwards
                            self.ycor = floor.ycor - self.height
                            self.y_vel = 0
                            self.on_ground = True

            if ceil and self.xcor + self.width > ceil.xcor and self.xcor < ceil.xcor + ceil.width:
                if self.ycor + self.height > ceil.ycor and self.ycor < ceil.ycor:
                    # if more than 1/10 of the entity's height is above the ceiling,
                    # and they are near the edge of the surface, let them go up
                    if abs(self.ycor - ceil.ycor) < self.height / 10 and \
                            (ceil.xcor - self.xcor > 1 or self.xcor + self.width - ceil.xcor + ceil.width > 1):
                        if self.y_vel < 0:  # if the entity is moving upwards
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
        """Runs update checks on the entity.

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
        """Draws the entity to the screen.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)

        pygame.draw.rect(
            screen,
            self.color,
            (self.xcor, self.ycor, self.width, self.height)
        )


class Player(Entity):
    """Player class.
    """

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        speed: int | float,
        health: int,
        max_health: int,
        color: Tuple[int],
        weapon: None = None,
    ) -> None:
        """Initializer for the entity object.

        :param xcor: The x position of the entity object.
        :type xcor: int | float
        :param ycor: The y position of the entity object.
        :type ycor: int | float
        :param width: The width of the entity object.
        :type width: int | float
        :param height: The height of the entity object.
        :type height: int | float
        :param speed: The speed of the entity object.
        :type speed: int | float
        :param health: The health of the entity object.
        :type health: int
        :param max_health: The maximum health of the entity object.
        :type max_health: int
        :param color: The color of the entity object.
        :type color: Tuple[int]
        :param weapon: The weapon of the player.
        :type weapon: Weapon | None
        """

        super().__init__(
            xcor,
            ycor,
            width,
            height,
            speed,
            health,
            max_health,
            color
        )
        self.weapon = None

    def take_damage(
        self,
        dmg: int
    ) -> None:
        """Damages the player with the given damage.

        :param dmg: The amount of damage to take.
        :type dmg: int
        """

        self.health -= dmg
        if self.health < 1:
            self.health = 0

    def update(
        self,
        dt: int | float,
        platforms: List[Surface]
    ) -> None:
        """Runs update checks on the entity.

        :param dt: Delta time.
        :type dt: int | float
        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: List[Surface]
        """

        if self.health == 0:
            # TODO
            ...
        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

        self.check_surface_collision(platforms)
