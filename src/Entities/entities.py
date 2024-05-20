"""Entities/entities.py

Module containing entity related functionality.
"""

from typing import List, Tuple

import pygame
from ..Internal import check_type, GRAVITY_ACCELERATION, Hitbox
from ..Level import Surface


class Entity(Hitbox):
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

        super().__init__(xcor, ycor, width, height, color)

        self.speed: int | float = speed
        self.y_vel: int | float = 0
        self.on_ground: bool = False
        self.double_jump_debounce: bool = True

        self.health: int | float = health
        self.max_health: int | float = max_health

    # movement

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
        """Increases the entity's vertical velocity if on the ground.
        """

        if self.on_ground:
            self.y_vel -= 500
            self.on_ground = False

    # updates

    def check_surface_collisions(
        self,
        platforms: List[Surface]
    ) -> None:
        """Run checks on the entity's collisions with other objects.

        :param surfaces: A list of surfaces necessary for collision checks.
        :type surfaces: List[Surface]
        """

        check_type(platforms, list)

        for platform in platforms:
            check_type(platform, Surface)

            # vvv welcome to hell vvv

            if platform.has_collision and self.colliderect(platform):
                collision_area = self.clip(platform)

                # vertical collisions checks (floor and ceiling)
                if collision_area.width - 3 > collision_area.height:
                    # top of platform collision
                    if self.coords.bottom() > platform.coords.top() and self.coords.top() < platform.coords.top():
                        self.ycor = platform.coords.top() - self.height
                        self.y_vel = 0
                        self.on_ground = True
                        self.can_jump = True
                    # bottom of platform collision
                    elif self.coords.top() < platform.coords.bottom() and self.coords.bottom() > platform.coords.bottom():
                        self.ycor = platform.coords.bottom()
                        self.y_vel = 0

                # horizontal collisions checks (left and right walls)
                if collision_area.height > collision_area.width - 3:
                    if self.coords.right() > platform.coords.left() and self.coords.left() < platform.coords.left():
                        self.xcor = platform.coords.left() - self.width
                    elif self.coords.left() < platform.coords.right() and self.coords.right() > platform.coords.right():
                        self.xcor = platform.coords.right()

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

        self.topleft = (self.xcor, self.ycor)
        self.coords.update(self.xcor, self.ycor)

        self.check_surface_collisions(platforms)

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

        self.weapon: None = None

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
        platforms: List[Surface],
        screen: pygame.Surface
    ) -> None:
        """Runs update checks on the player.

        :param dt: Delta time.
        :type dt: int | float
        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: List[Surface]
        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        if self.health == 0:
            # TODO
            ...

        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

        self.topleft = (self.xcor, self.ycor)
        self.coords.update(self.xcor, self.ycor)

        self.check_surface_collisions(platforms)
