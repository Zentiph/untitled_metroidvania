"""player.py

Module containing player related functionality.
"""

import pygame
from ..Internal import check_type


class Player:
    """A class representing the player object.
    """

    def __init__(
        self,
        x: int | float,
        y: int | float
    ) -> None:
        """Initializer for the player object.

        :param x: The x position of the player object.
        :type x: int
        :param y: The y position of the player object.
        :type y: int
        """

        # type checking

        self.hitbox = {
            'x': x,
            'y': y,
            'width': 40,
            'height': 40
        }
