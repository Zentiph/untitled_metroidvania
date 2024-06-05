"""Player/player.py

Module containing player related functionality.
"""

from typing import Tuple

import pygame

from ..Internal import GRAVITY_ACCELERATION, Hitbox, check_type
from ..Level import Group, Lava, Platform, Spike
from ..Stages import grid_to_stage, TextInfo


# pylint: disable=too-many-instance-attributes
class Player(Hitbox):
    """Base class for player objects."""

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
        """Initializer for the player object.

        :param xcor: The x position of the player object.
        :type xcor: int | float
        :param ycor: The y position of the player object.
        :type ycor: int | float
        :param width: The width of the player object.
        :type width: int | float
        :param height: The height of the player object.
        :type height: int | float
        :param speed: The speed of the player object.
        :type speed: int | float
        :param health: The health of the player object.
        :type health: int
        :param max_health: The maximum health of the player object.
        :type max_health: int
        :param has_collision: Whether the player object has collision.
        :type has_collision: bool, optional
        :param color: The color of the player object.
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

        self.facing_left: bool = False
        self.facing_right: bool = True

        self.grid_xcor: int = 1
        self.grid_ycor: int = 1
        self.stage: int | str = 1

        # i-frames used when taking damage
        self.i_frames: int = 0

    # movement

    def move_left(self, dt: float) -> None:
        """Moves the player left.

        :param dt: Delta time.
        :type dt: float
        """

        check_type(dt, int, float)
        self.xcor -= self.speed * dt

        self.facing_left = True
        self.facing_right = False

    def move_right(self, dt: float) -> None:
        """Moves the player right.

        :param dt: Delta time.
        :type dt: float
        """

        check_type(dt, int, float)
        self.xcor += self.speed * dt

        self.facing_left = False
        self.facing_right = True

    def jump(self) -> None:
        """Increases the player's vertical velocity if on the ground."""

        if self.on_ground:
            self.y_vel -= 500
            self.on_ground = False
            self.double_jump_debounce = False

    def double_jump(self) -> None:
        """Increments the player's vertical velocity if not
        on the ground and the double jump is available.
        """

        if not self.on_ground and not self.double_jump_debounce:
            self.y_vel = -500
            self.double_jump_debounce = True

    def take_damage(self, dmg: int) -> None:
        """Handles cases when the player takes damage.

        :param dmg: The amount of damage taken.
        :type dmg: int
        """

        if not self.i_frames:
            self.health -= dmg
            self.health = 0 if self.health < 0 else self.health
            self.i_frames = 10

            if self.health == 0:
                self.xcor = 800 - self.width / 2
                self.ycor = 540 - self.height
                self.grid_xcor, self.grid_ycor = (1, 0)

    # updates

    def check_platform_collisions(self, platforms: Group) -> None:
        """Run checks on the player's collisions with other objects.

        :param platforms: A list of platforms necessary for collision checks.
        :type platforms: Group
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

                        if self.facing_right:
                            self.xcor = platform.coords.left() - self.width
                        elif self.facing_left:
                            self.xcor = platform.coords.right()

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

                    # bottom of platform collision
                    elif (
                        self.coords.top() < platform.coords.bottom()
                        and self.coords.bottom() > platform.coords.bottom()
                    ):
                        self.ycor = platform.coords.bottom()
                        self.y_vel = 0

    def check_spike_collisions(self, spikes: Group | None) -> None:
        """Checks for collisions between the player and the given Spikes.

        :param spikes: A Group of Spike objects.
        :type spikes: Group
        """

        if spikes is None:
            return

        check_type(spikes, Group)

        for spike in spikes:
            check_type(spike, Spike)

            if (
                self.has_collision
                and spike.has_collision
                and self.colliderect(spike.hitbox)
            ):
                self.y_vel = -500
                self.take_damage(1)

    def check_lava_collisions(self, lavas: Group | None) -> None:
        """Checks for collisions between the player and the given Lavas.

        :param lavas: A Group of Lava objects.
        :type lavas: Group
        """

        if lavas is None:
            return

        check_type(lavas, Group)

        for lava in lavas:
            check_type(lava, Lava)

            if self.has_collision and lava.has_collision and self.colliderect(lava):
                self.y_vel = -500
                self.take_damage(5)

    def update_(
        self,
        dt: float,
        objects: Tuple[
            Tuple[int, int],
            Group,
            Group | None,
            Group | None,
            Tuple[TextInfo, ...] | None,
        ],
    ) -> None:
        """Runs update checks on the player.

        :param dt: Delta time.
        :type dt: float
        :param objects: A list of objects necessary for collision checks.
        :type objects: Tuple[Group, Group | None, Group | None, TextInfo | None]
        """

        self.y_vel += GRAVITY_ACCELERATION * dt
        self.ycor += self.y_vel * dt
        self.on_ground = False

        # pylint: disable=attribute-defined-outside-init
        self.topleft = (int(self.xcor), int(self.ycor))
        # pylint: enable=attribute-defined-outside-init
        self.coords.update(self.xcor, self.ycor)

        self.interp(dt)

        # collision detection
        self.check_platform_collisions(objects[1])
        self.check_spike_collisions(objects[2])
        self.check_lava_collisions(objects[3])

        # room transitions
        if self.coords.is_off_screen_right(self.width):
            # disable interp to prevent bugs
            self.interp_data.moving = False

            self.xcor = 0
            self.grid_xcor += 1
        elif self.coords.is_off_screen_left(self.width):
            # disable interp to prevent bugs
            self.interp_data.moving = False

            self.xcor = 1600 - self.width
            self.grid_xcor -= 1
        elif self.coords.is_off_screen_up(self.width):
            # disable interp to prevent bugs
            self.interp_data.moving = False

            self.ycor = 800 - self.height
            self.grid_ycor -= 1
        elif self.coords.is_off_screen_down(self.width):
            # disable interp to prevent bugs
            self.interp_data.moving = False

            self.ycor = 0
            self.grid_ycor += 1

        self.stage = grid_to_stage((self.grid_xcor, self.grid_ycor))

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the player to the screen.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)

        pygame.draw.rect(
            screen, self.color, (self.xcor, self.ycor, self.width, self.height)
        )
