"""Internal.hitboxes.py

Module containing hitbox functionality.
"""

from typing import Callable, Tuple, Union

import pygame

from . import interp
from .checks import check_type
from .constants import SCREEN_HEIGHT, SCREEN_WIDTH

# custom EasingFunction type used for documentation
EasingFunction = Callable[[float], float]


class Coordinates:
    """Helper class for storing coordinates and related functions."""

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
    ) -> None:
        """Initializer for a Coordinates object.

        :param xcor: The x coordinate.
        :type xcor: int | float
        :param ycor: The y coordinate.
        :type ycor: int | float
        :param width: The width.
        :type width: int | float
        :param height: The height.
        :type height: int | float
        """

        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(width, int, float)
        check_type(height, int, float)

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.width: int | float = width
        self.height: int | float = height

        self.y_vel: int | float = 0

    def update(self, xcor: int | float, ycor: int | float) -> None:
        """Updates the Coordinates class with new values.

        :param xcor: The x coordinate.
        :type xcor: int | float
        :param ycor: The y coordinate.
        :type ycor: int | float
        """

        check_type(xcor, int, float)
        check_type(ycor, int, float)

        self.xcor = xcor
        self.ycor = ycor

    def left(self) -> int | float:
        """Gets the leftmost x-coordinate of the entity."""

        return self.xcor

    def right(self) -> int | float:
        """Gets the rightmost x-coordinate of the entity."""

        return self.xcor + self.width

    def center_x(self) -> int | float:
        """Gets the center x-coordinate of the entity."""

        return (2 * self.xcor + self.width) / 2

    def top(self) -> int | float:
        """Gets the topmost x-coordinate of the entity."""

        return self.ycor

    def bottom(self) -> int | float:
        """Gets the bottommost x-coordinate of the entity."""

        return self.ycor + self.height

    def center_y(self) -> int | float:
        """Gets the center y-coordinate of the entity."""

        return (2 * self.ycor + self.height) / 2

    def top_left(self) -> Tuple[Union[int, float], Union[int, float]]:
        """Gets the top left coordinates of the entity."""

        return self.xcor, self.ycor

    def top_right(self) -> Tuple[Union[int, float], Union[int, float]]:
        """Gets the top right coordinates of the entity."""

        return self.xcor + self.width, self.ycor

    def bottom_left(self) -> Tuple[Union[int, float], Union[int, float]]:
        """Gets the bottom left coordinates of the entity."""

        return self.xcor, self.ycor + self.height

    def bottom_right(self) -> Tuple[Union[int, float], Union[int, float]]:
        """Gets the bottom right coordinates of the entity."""

        return self.xcor + self.width, self.ycor + self.height

    def center(self) -> Tuple[Union[int, float], Union[int, float]]:
        """Gets the center coordinates of the entity."""

        return (2 * self.xcor + self.width) / 2, (2 * self.ycor + self.height) / 2

    def is_off_screen_right(self) -> bool:
        """Checks if the entity is off-screen to the right.

        :return: Whether the entity is off-screen to the right.
        :rtype: bool
        """

        if self.xcor + self.width > SCREEN_WIDTH:
            return True
        return False

    def is_off_screen_left(self) -> bool:
        """Checks if the entity is off-screen to the left.

        :return: Whether the entity is off-screen to the left.
        :rtype: bool
        """

        if self.xcor < 0:
            return True
        return False

    def is_off_screen_up(self) -> bool:
        """Checks if the entity is off-screen above.

        :return: Whether the entity is off-screen above.
        :rtype: bool
        """

        if self.ycor + self.height < 0:
            return True
        return False

    def is_off_screen_down(self) -> bool:
        """Checks if the entity is off-screen below.

        :return: Whether the entity is off-screen below.
        :rtype: bool
        """

        if self.ycor > SCREEN_HEIGHT:
            return True
        return False

    def is_off_screen(self) -> bool:
        """Checks if the entity is off-screen.

        :return: Whether the entity is off-screen.
        :rtype: bool
        """

        if (
            self.xcor < 0
            or self.xcor + self.width > SCREEN_WIDTH
            or self.ycor + self.height < 0
            or self.ycor > SCREEN_HEIGHT
        ):
            return True
        return False


class InterpolationData:
    """Helper class for storing interpolation data."""

    def __init__(
        self,
        initial_pos: Tuple[Union[int, float], Union[int, float]],
        target_pos: Tuple[Union[int, float], Union[int, float]],
        duration: int | float,
        easing_type: EasingFunction = interp.linear,
    ) -> None:
        """ "Initializer for the InterpolationData object.

        :param initial_pos: The initial coordinates.
        :type initial_pos: Tuple[Union[int, float], Union[int, float]]
        :param target_pos: The target coordinates.
        :type target_pos: Tuple[Union[int, float], Union[int, float]]
        :param duration: The duration of the interpolation in seconds.
        :type duration: int | float
        :param easing_type: The easing type of the interpolation.
        :type easing_type: EasingFunction, optional
        """

        check_type(initial_pos, tuple)
        for v in initial_pos:
            check_type(v, int, float)
        check_type(target_pos, tuple)
        for v in target_pos:
            check_type(v, int, float)
        check_type(duration, int, float)

        self.initial_pos: Tuple[Union[int, float], Union[int, float]] = initial_pos
        self.target_pos: Tuple[Union[int, float], Union[int, float]] = target_pos
        self.duration: int | float = duration

        self.easing_type: EasingFunction = easing_type

        self.elapsed_time: int | float = 0
        self.moving: bool = False


class Hitbox(pygame.Rect):
    """Base class for all hitboxes."""

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        has_collision: bool = True,
        color: Tuple[int, int, int] = (0, 255, 0),
    ) -> None:
        """Initializer for the hitbox object.

        :param xcor: The x position of the hitbox object.
        :type xcor: int | float
        :param ycor: The y position of the hitbox object.
        :type ycor: int | float
        :param width: The width of the hitbox object.
        :type width: int | float
        :param height: The height of the hitbox object.
        :type height: int | float
        :param has_collision: Whether the hitbox has collision.
        :type has_collision: bool
        :param color: The color of the hitbox object.
        :type color: Tuple[int]
        """

        # type checking
        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(width, int, float)
        check_type(height, int, float)
        check_type(has_collision, bool)
        check_type(color, tuple)
        for v in color:
            check_type(v, int)
            if v < 0 or v > 255:
                raise ValueError(f"Color value {v} is out of range.")
        if len(color) != 3:
            raise ValueError(f"Color tuple must be of length 3, not {len(color)}.")

        super().__init__(xcor, ycor, width, height)

        self.xcor: int | float = xcor
        self.ycor: int | float = ycor
        self.y_vel: int | float = 0

        self.has_collision = has_collision
        self.color: Tuple[int, int, int] = color

        self.coords = Coordinates(xcor, ycor, width, height)
        self.interp_data = InterpolationData((xcor, ycor), (xcor, ycor), 0)

    # movement

    def moveto(
        self,
        xcor: int | float,
        ycor: int | float,
        duration: int | float,
        easing_type: EasingFunction,
        disable_collision: bool = True,
    ) -> None:
        """Moves the hitbox to the specified coordinates.

        :param xcor: The x-coordinate of the destination.
        :type xcor: int | float
        :param ycor: The y-coordinate of the destination.
        :type ycor: int | float
        :param easing_type: The easing function to use.
        :type easing_type: EasingFunction
        :param disable_collision: Whether to disable collision of the moving object.
        :type disable_collision: bool, optional
        """

        check_type(xcor, int, float)
        check_type(ycor, int, float)
        check_type(duration, int, float)
        check_type(disable_collision, bool)

        if disable_collision:
            self.has_collision = False

        self.interp_data.initial_pos = (self.xcor, self.ycor)
        self.interp_data.target_pos = (xcor, ycor)
        self.interp_data.duration = duration
        self.interp_data.easing_type = easing_type
        self.interp_data.elapsed_time = 0
        self.interp_data.moving = True

    # updates

    def interp(self, dt: int | float) -> None:
        """Updates the hitbox's position.

        :param dt: Delta time.
        :type dt: int | float
        """

        if self.interp_data.moving:
            self.y_vel = 0
            self.interp_data.elapsed_time += dt

            if self.interp_data.elapsed_time >= self.interp_data.duration:
                self.xcor = self.interp_data.target_pos[0]
                self.ycor = self.interp_data.target_pos[1]
                self.interp_data.moving = False
                self.has_collision = True
            else:
                t = self.interp_data.elapsed_time / self.interp_data.duration

                t_eased = self.interp_data.easing_type(t)

                self.xcor = interp.lerp(
                    self.interp_data.initial_pos[0],
                    self.interp_data.target_pos[0],
                    t_eased,
                )
                self.ycor = interp.lerp(
                    self.interp_data.initial_pos[1],
                    self.interp_data.target_pos[1],
                    t_eased,
                )

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the hitbox to the screen.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)

        pygame.draw.rect(
            screen, self.color, (self.xcor, self.ycor, self.width, self.height)
        )
