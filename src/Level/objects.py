"""Level.surfaces.py

Module containing surface functionality.
"""

from typing import Any, Dict, Iterator, Tuple, Union

import pygame

from ..Internal import check_type, Hitbox


class Platform(Hitbox):
    """Class used to create platform objects."""

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        has_collision: bool = True,
        color: Tuple[int, int, int] = (0, 0, 255),
    ) -> None:
        """Initializer for Platform objects.

        :param x: The x position of the platform.
        :type x: int | float
        :param y: The y position of the platform.
        :type y: int | float
        :param width: The width of the platform.
        :type width: int | float
        :param height: The height of the platform.
        :type height: int | float
        :param has_collision: Whether the platform has collision.
        :type has_collision: bool, optional
        :param color: The color of the platform.
        :type color: Tuple[int], optional
        """

        super().__init__(xcor, ycor, width, height, has_collision, color)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the platform to the screen.

        :param screen: The screen to draw the platform.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)
        pygame.draw.rect(
            screen, self.color, (self.left, self.top, self.width, self.height)
        )


class Spike(Hitbox):
    """Class used to create Spike objects."""

    def __init__(
        self,
        xcor: int | float,
        ycor: int | float,
        width: int | float,
        height: int | float,
        has_collision: bool = True,
        color: Tuple[int, int, int] = (255, 128, 0),
    ) -> None:
        """Initializer for Spike objects.

        :param x: The x position of the spike.
        :type x: int | float
        :param y: The y position of the spike.
        :type y: int | float
        :param width: The width of the spike.
        :type width: int | float
        :param height: The height of the spike.
        :type height: int | float
        :param has_collision: Whether the spike has collision.
        :type has_collision: bool, optional
        :param color: The color of the spike.
        :type color: Tuple[int], optional
        """

        super().__init__(xcor, ycor, width, height, has_collision, color)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the spike to the screen.

        :param screen: The screen to draw the spike.
        :type screen: pygame.Surface
        """

        check_type(screen, pygame.Surface)

        # calculate the points of the spike
        p1: Tuple[Union[int, float], Union[int, float]] = (
            self.xcor,
            self.ycor + self.height,
        )
        p2: Tuple[Union[int, float], Union[int, float]] = (
            self.xcor + self.width / 2,
            self.ycor,
        )
        p3: Tuple[Union[int, float], Union[int, float]] = (
            self.xcor + self.width,
            self.ycor + self.height,
        )

        pygame.draw.polygon(screen, self.color, (p1, p2, p3))


class Group:
    """Groups together multiple Level objects."""

    def __init__(self, *objects: Any) -> None:
        """Initializes the Group with the given objects.

        :param objects: The objects to group.
        :type objects: Any
        """

        self.objects: Dict[str, Any] = {}
        self._name_count: Dict[str, int] = {}

        for obj in objects:
            self._add_objects(obj)

        self.index = 0

    def __getattr__(self, name: str) -> Any:
        """Grants access to grouped objects by their class name.

        :param name: The name of the object to access.
        :type name: str
        :return: The object associated with the given name.
        :rtype: Any
        """

        try:
            return self.objects[name]
        except KeyError as e:
            raise AttributeError(
                f"'Group' has no object with the name '{name}'."
            ) from e

    def __len__(self) -> int:
        """Returns the number of objects in the group.

        :return: The number of objects in the group.
        :rtype: int
        """

        return len(self.objects)

    def __iter__(self) -> Iterator:
        """Allows iteration over the group objects.

        :return: An iterator over the objects in the group.
        :rtype: Iterator
        """

        return iter(self.objects.values())

    def __contains__(self, item: Union[str, Any]) -> bool:
        """Checks if an object or name is in the group.

        :param item: The object or name to check.
        :type item: Union[str, Any]
        :return: True if the object or name is in the group, False otherwise.
        :rtype: bool
        """

        if isinstance(item, str):
            return item in self.objects
        return item in self.objects.values()

    def _add_objects(self, *objects: Any) -> None:
        """Internal method that adds the objects to the Group.

        :param objects: The objects to add.
        """

        for obj in objects:
            class_name = obj.__class__.__name__.lower()
            if class_name in self._name_count:
                self._name_count[class_name] += 1
                unique_name = f"{class_name}_{self._name_count[class_name]}"
            else:
                self._name_count[class_name] = 0
                unique_name = class_name

            self.objects[unique_name] = obj

    def add(self, *objects: Any) -> None:
        """Adds the objects to the Group.

        :param objects: The objects to add.
        :type objects: Any
        """

        self._add_objects(*objects)

    def clear(self) -> None:
        """Removes all objects from the group."""

        self.objects.clear()
        self._name_count.clear()

    def update(self, **kwargs) -> None:
        """Updates properties of all objects in the group.

        :param kwargs: The properties to update and their new values.
        """

        for obj in self.objects.values():
            for k, v in kwargs.items():
                if hasattr(obj, k):
                    setattr(obj, k, v)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws all drawable objects in the group to the screen.

        :param screen: The screen to draw the objects on.
        :type screen: pygame.Surface
        """

        for obj in self.objects.values():
            if hasattr(obj, "draw") and callable(obj.draw):
                obj.draw(screen)
