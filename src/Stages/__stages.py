"""Stages.stages.py

Module containing all the preset stages for the game.
"""

from typing import Dict, Tuple, Union

from ..Internal import SCREEN_HEIGHT, SCREEN_WIDTH
from ..Level import Group, Platform, Spike

__all__ = ["STAGES", "TextInfo", "DEBUG", "STAGE1"]


class TextInfo:
    """Contains info about text to write to the screen."""

    def __init__(
        self,
        msg: str,
        xcor: int | float,
        ycor: int | float,
        size: int,
        color: Tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """Initializer for a TextInfo instance.

        :param msg: The message for the text to display.
        :type msg: str
        :param xcor: The x-coordinate of the text.
        :type xcor: int | float
        :param ycor: The y-coordinate of the text.
        :type ycor: int | float
        :param size: The size of the text.
        :type size: int
        :param color: The color of the text.
        :type color: Tuple[int, int, int], optional
        """

        self.msg = msg
        self.xcor = xcor
        self.ycor = ycor
        self.size = size
        self.color = color


DEBUG: Tuple[Group, Group | None, Group | None, TextInfo | None] = (
    # platforms
    Group(
        Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50),
        Platform(0, 0, SCREEN_WIDTH, 50),
        Platform(0, 0, 50, SCREEN_HEIGHT),
        Platform(SCREEN_WIDTH - 50, 0, 50, SCREEN_HEIGHT),
    ),
    None,
    None,
    None,
)


# STAGE FORMAT
#
# platforms in a group first
# then spikes
# then lava
# then text

# IMPORTANT: MAKE SURE THAT IF THE STAGE DOES NOT HAVE
# LAVA, SPIKES, OR TEXT, TO LEAVE THAT PART AS 'None'

STAGE1: Tuple[Group, Group | None, Group | None, TextInfo | None] = (
    # platforms
    Group(
        Platform(0, 850, 1600, 50),  # floor
        Platform(0, 0, 1600, 50),  # ceiling
        Platform(0, 0, 50, 450),  # left wall
        Platform(0, 800, 50, 100),  # bottom ledge
        Platform(0, 450, 50, 350, False, (50, 50, 255)),  # walkable wall
    ),
    None,
    None,
    TextInfo(
        "Walk with A and D or ARROW KEYS",
        SCREEN_WIDTH / 2 - 650,
        SCREEN_HEIGHT / 2 - 200,
        100,
    ),
)

STAGE2: Tuple[Group, Group | None, Group | None, TextInfo | None] = (
    # platforms
    Group(
        Platform(0, 850, 1600, 50),  # floor
        Platform(0, 0, 1600, 50),  # ceiling
        Platform(0, 0, 50, 450),  # left wall
        Platform(0, 800, 50, 100),  # bottom ledge
        Platform(500, 800, 100, 100),
        Platform(1000, 800, 100, 100),
    ),
    # spikes
    Group(
        Spike(600, 825, 25, 25),
        Spike(625, 825, 25, 25),
        Spike(650, 825, 25, 25),
        Spike(675, 825, 25, 25),
        Spike(700, 825, 25, 25),
        Spike(725, 825, 25, 25),
        Spike(750, 825, 25, 25),
        Spike(775, 825, 25, 25),
        Spike(800, 825, 25, 25),
        Spike(825, 825, 25, 25),
        Spike(850, 825, 25, 25),
        Spike(875, 825, 25, 25),
        Spike(900, 825, 25, 25),
        Spike(925, 825, 25, 25),
        Spike(950, 825, 25, 25),
        Spike(975, 825, 25, 25),
    ),
    None,
    TextInfo(
        "Jump with W, SPACE, or UP ARROW",
        SCREEN_WIDTH / 2 - 650,
        SCREEN_HEIGHT / 2 - 200,
        100,
    ),
)

STAGES: Dict[
    Union[int, str], Tuple[Group, Group | None, Group | None, TextInfo | None]
] = {
    "DEBUG": DEBUG,
    1: STAGE1,
    2: STAGE2,
}
