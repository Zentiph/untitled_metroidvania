"""Entities/entities.py

Module containing entity related functionality.
"""

from typing import Tuple

import pygame
from ..Internal import check_type, GRAVITY_ACCELERATION, Hitbox
from ..Level import Group, Platform


class Entity(Hitbox):
    """Base class for entity objects."""

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        speed: int | float,
        health: int,
        max_health: int,
        has_collision: bool = True,
        color: Tuple[int, int, int] = (255, 255, 255),
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
        :param has_collision: Whether the entity object has collision.
        :type has_collision: bool, optional
        :param color: The color of the entity object.
        :type color: Tuple[int]
        """

        # type checking
        check_type(speed, int, float)
        check_type(health, int)
        check_type(max_health, int)

        super().__init__(xcor, ycor, width, height, has_collision, color)

        self.speed: int | float = speed
        self.on_ground: bool = False
        self.double_jump_debounce: bool = True

        self.health: int | float = health
        self.max_health: int | float = max_health

    # movement

    def move_left(self, dt: float) -> None:
        """Moves the entity left.

        :param dt: Delta time.
        :type dt: float
        """

        check_type(dt, int, float)
        self.xcor -= self.speed * dt

    def move_right(self, dt: float) -> None:
        """Moves the entity right.

        :param dt: Delta time.
        :type dt: float
        """

        check_type(dt, int, float)
        self.xcor += self.speed * dt

    def jump(self) -> None:
        """Increases the entity's vertical velocity if on the ground."""

        if self.on_ground:
            self.y_vel -= 500
            self.on_ground = False
            self.double_jump_debounce = False

    def double_jump(self) -> None:
        """Increments the entity's vertical velocity if not
        on the ground and the double jump is available.
        """

        if not self.on_ground and not self.double_jump_debounce:
            self.y_vel = -500
            self.double_jump_debounce = True

    # updates

    def check_platform_collisions(self, platforms: Group) -> None:
        """Run checks on the entity's collisions with other objects.

        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: List[Platform]
        """

        check_type(platforms, Group)

        for platform in platforms:
            check_type(platform, Platform)

            # vvv welcome to hell vvv

            if (
                self.has_collision
                and platform.has_collision
                and self.colliderect(platform)
            ):
                collision_area = self.clip(platform)

                # horizontal collisions checks (left and right walls)
                if collision_area.height > collision_area.width - 3:
                    if (
                        self.coords.right() > platform.coords.left()
                        and self.coords.right() < platform.coords.center_x()
                    ):
                        # reset interp data to stop movement if a collision is detected
                        self.interp_data.moving = False
                        self.interp_data.target_pos = (self.xcor, self.ycor)

                        self.xcor = platform.coords.left() - self.width

                    elif (
                        self.coords.left() < platform.coords.right()
                        and self.coords.left() > platform.coords.center_x()
                    ):
                        # reset interp data to stop movement if a collision is detected
                        self.interp_data.moving = False
                        self.interp_data.target_pos = (self.xcor, self.ycor)

                        self.xcor = platform.coords.right()

                # vertical collisions checks (floor and ceiling)
                if collision_area.width - 3 > collision_area.height:
                    # top of platform collision
                    if (
                        self.coords.bottom() > platform.coords.top()
                        and self.coords.top() < platform.coords.top()
                    ):
                        self.ycor = platform.coords.top() - self.height
                        self.y_vel = 0
                        self.on_ground = True

                        # set the interp target pos y-coordinate to the player's coordinate
                        # to prevent the jittery behavior when dashing near a floor/ceiling.
                        # basically the interp function kept moving the player into the block after
                        # the collision moves the player out. this fixes that
                        self.interp_data.target_pos = (
                            self.interp_data.target_pos[0],
                            self.ycor,
                        )

                    # bottom of platform collision
                    elif (
                        self.coords.top() < platform.coords.bottom()
                        and self.coords.bottom() > platform.coords.bottom()
                    ):
                        self.ycor = platform.coords.bottom()
                        self.y_vel = 0

                        # set the interp target pos y-coordinate to the player's coordinate
                        # to prevent the jittery behavior when dashing near a floor/ceiling.
                        # basically the interp function kept moving the player into the block after
                        # the collision moves the player out. this fixes that
                        self.interp_data.target_pos = (
                            self.interp_data.target_pos[0],
                            self.ycor,
                        )

    def update_(self, dt: float, platforms: Group) -> None:
        """Runs update checks on the entity.

        :param dt: Delta time.
        :type dt: float
        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: List[Platform]
        """

        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

        # pylint: disable=attribute-defined-outside-init
        self.topleft = (int(self.xcor), int(self.ycor))
        # pylint: enable=attribute-defined-outside-init
        self.coords.update(self.xcor, self.ycor)

        self.check_platform_collisions(platforms)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the entity to the screen.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)

        pygame.draw.rect(
            screen, self.color, (self.xcor, self.ycor, self.width, self.height)
        )


class Player(Entity):
    """Player class."""

    def take_damage(self, dmg: int) -> None:
        """Damages the player with the given damage.

        :param dmg: The amount of damage to take.
        :type dmg: int
        """

        self.health -= dmg
        if self.health < 1:
            self.health = 0

    # it's named update_ to prevent overriding an existing class method of pygame.Rect
    def update_(
        self,
        dt: float,
        platforms: Group,
    ) -> None:
        """Runs update checks on the player.

        :param dt: Delta time.
        :type dt: float
        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: List[Platform]
        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        if self.health == 0:
            # TODO
            ...

        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

        # pylint: disable=attribute-defined-outside-init
        self.topleft = (int(self.xcor), int(self.ycor))
        # pylint: disable=attribute-defined-outside-init
        self.coords.update(self.xcor, self.ycor)

        self.interp(dt)
        self.check_platform_collisions(platforms)
