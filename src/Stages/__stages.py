"""Stages.stages.py

Module containing all the preset stages for the game.
"""

from typing import Dict, Tuple, Union

from ..Internal import SCREEN_HEIGHT, SCREEN_WIDTH
from ..Level import Group, Lava, Platform, Spike

__all__ = ["STAGES", "TextInfo", "grid_to_stage", "DEBUG", "STAGE1"]


class StageNotFoundError(Exception):
    pass


class TextInfo:
    """Contains info about text to write to the screen."""

    def __init__(
        self,
        msg: str,
        xcor: int | float,
        ycor: int | float,
        size: int = 100,
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
        :type size: int, optional
        :param color: The color of the text.
        :type color: Tuple[int, int, int], optional
        """

        self.msg = msg
        self.xcor = xcor
        self.ycor = ycor
        self.size = size
        self.color = color


def grid_to_stage(grid_location: Tuple[int, int]) -> int | str:
    """Returns the corresponding stage number for the grid location.

    :param grid_location: The location of the player on the grid.
    :type grid_location: Tuple[int, int]
    :return: The corresponding stage number.
    :rtype: int | str
    """

    match grid_location:
        # special stages
        case (-1, -1):
            return "DEBUG"
        case (1, 0):
            return "GAME_OVER"

        # regular stages
        case (1, 1):
            return 1
        case (2, 1):
            return 2

    # raise an error if the stage is not found
    raise StageNotFoundError


# SPECIAL STAGES

# TODO (MAYBE)
MENU: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
]

GAME_OVER: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (1, 0),
    # platforms
    Group(
        Platform(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100),  # floor
        Platform(0, 0, SCREEN_WIDTH, 100),  # ceiling
        Platform(-50, 0, 150, SCREEN_HEIGHT),  # left wall
        Platform(SCREEN_WIDTH - 100, 0, 150, SCREEN_HEIGHT),  # right wall
    ),
    # spikes
    None,
    # lava
    None,
    (
        TextInfo("GAME OVER", SCREEN_WIDTH / 2 - 250, 150),
        TextInfo("Press R to restart", SCREEN_WIDTH / 2 - 325, 220),
    ),
)


DEBUG: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location (placeholder to match the other formats, unnecessary for most special stages)
    (-1, -1),
    # platforms
    Group(
        Platform(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH - 400, 100),  # floor
        Platform(0, 0, SCREEN_WIDTH, 100),  # ceiling
        Platform(-50, 0, 150, SCREEN_HEIGHT),  # left wall
        Platform(SCREEN_WIDTH - 100, 0, 150, SCREEN_HEIGHT),  # right wall
    ),
    # spikes
    Group(
        Spike(600, 750, 50, 50),
        Spike(650, 750, 50, 50),
        Spike(700, 750, 50, 50),
        Spike(750, 750, 50, 50),
    ),
    # lava
    Group(Lava(SCREEN_WIDTH - 400, SCREEN_HEIGHT - 100, 300, 100)),
    (TextInfo("DEBUG ROOM", SCREEN_WIDTH / 2 - 325, 150),),
)


# STAGE FORMAT
#
# grid coordinate tuple
# platforms in a group (MAKE SURE WALLS ARE AT LEAST 150 WIDE TO PREVENT DASH-THROUGH)
# then spikes
# then lava
# then text

# IMPORTANT: MAKE SURE THAT IF THE STAGE DOES NOT HAVE
# LAVA, SPIKES, OR TEXT, TO LEAVE THAT PART AS 'None'

STAGE1: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (1, 1),
    # platforms
    Group(
        Platform(0, 800, 1600, 100),  # floor
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(-50, 0, 150, 450),  # left wall
        Platform(1500, 0, 150, 600),  # right wall
        Platform(0, 700, 100, 100),  # bottom ledge
        Platform(0, 400, 100, 300, False, (30, 30, 255)),  # walkable wall
    ),
    None,
    None,
    (
        TextInfo(
            "Walk with A and D or ARROW KEYS",
            SCREEN_WIDTH / 2 - 650,
            SCREEN_HEIGHT / 2 - 200,
        ),
    ),
)

STAGE2: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (2, 1),
    # platforms
    Group(
        Platform(0, 800, 1600, 100),  # floor
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(0, 0, 100, 600),  # left wall
        Platform(1500, 0, 100, 600),  # right wall
        Platform(450, 700, 150, 150),  # bottom ledge left
        Platform(1000, 700, 150, 150),  # bottom ledge right
        Platform(725, 600, 150, 50),  # floating platform
    ),
    # spikes
    Group(
        Spike(600, 750, 50, 50),
        Spike(650, 750, 50, 50),
        Spike(700, 750, 50, 50),
        Spike(750, 750, 50, 50),
        Spike(800, 750, 50, 50),
        Spike(850, 750, 50, 50),
        Spike(900, 750, 50, 50),
        Spike(950, 750, 50, 50),
    ),
    None,
    (
        TextInfo(
            "Jump with W, SPACE, or UP ARROW",
            SCREEN_WIDTH / 2 - 650,
            SCREEN_HEIGHT / 2 - 200,
        ),
    ),
)

STAGES: Dict[
    Union[int, str],
    Tuple[
        Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
    ],
] = {
    # special stages
    "DEBUG": DEBUG,
    "GAME_OVER": GAME_OVER,
    # regular stages
    1: STAGE1,
    2: STAGE2,
}
