"""Stages.stages.py

Module containing all the preset stages for the game.
"""

# this whole module kinda sucks and isn't ideal,
# but it's the most elegant way I could think of
# doing this with 3 days left.

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
        Platform(0, 400, 100, 300),  # not walkable wall
        # Platform(0, 400, 100, 300, False, (30, 30, 255)),  # walkable wall
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
        Platform(-50, 0, 150, 600),  # left wall
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

STAGE3: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (3, 1),
    # platforms
    Group(
        Platform(0, 800, 450, 100),  # floor left side
        Platform(1100, 800, 500, 100),  # floor right side
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(-50, 0, 150, 600),  # left wall
        Platform(1500, 0, 150, 600),  # right wall
        Platform(700, 600, 150, 300),  # center wall
        Platform(0, 850, 1600, 50),  # long floor
    ),
    Group(
        # left spike pit
        Spike(450, 800, 50, 50),
        Spike(500, 800, 50, 50),
        Spike(550, 800, 50, 50),
        Spike(600, 800, 50, 50),
        Spike(650, 800, 50, 50),
        # right spike pit
        Spike(850, 800, 50, 50),
        Spike(900, 800, 50, 50),
        Spike(950, 800, 50, 50),
        Spike(1000, 800, 50, 50),
        Spike(1050, 800, 50, 50),
    ),
    None,
    (
        TextInfo(
            "Double-jump by pressing", SCREEN_WIDTH / 2 - 455, SCREEN_HEIGHT / 2 - 300
        ),
        TextInfo(
            "W, SPACE, or UP ARROW", SCREEN_WIDTH / 2 - 460, SCREEN_HEIGHT / 2 - 200
        ),
        TextInfo(
            "again when in midair",
            SCREEN_WIDTH / 2 - 400,
            SCREEN_HEIGHT / 2 - 100,
        ),
    ),
)

STAGE4: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (4, 1),
    # platforms
    Group(
        Platform(0, 800, 300, 100),  # floor left side
        Platform(1300, 800, 300, 100),  # floor right side
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(-50, 0, 150, 600),  # left wall
        Platform(1500, 0, 150, 600),  # right wall
        Platform(700, 750, 200, 100),  # center wall
        Platform(0, 850, 1600, 50),  # long floor
    ),
    Group(
        # left spike pit
        Spike(300, 800, 50, 50),
        Spike(350, 800, 50, 50),
        Spike(400, 800, 50, 50),
        Spike(450, 800, 50, 50),
        Spike(500, 800, 50, 50),
        Spike(550, 800, 50, 50),
        Spike(600, 800, 50, 50),
        Spike(650, 800, 50, 50),
        # right spike pit
        Spike(900, 800, 50, 50),
        Spike(950, 800, 50, 50),
        Spike(1000, 800, 50, 50),
        Spike(1050, 800, 50, 50),
        Spike(1100, 800, 50, 50),
        Spike(1150, 800, 50, 50),
        Spike(1200, 800, 50, 50),
        Spike(1250, 800, 50, 50),
    ),
    None,
    (
        TextInfo(
            "Your double-jump has a small",
            SCREEN_WIDTH / 2 - 540,
            SCREEN_HEIGHT / 2 - 300,
        ),
        TextInfo(
            "cooldown before activating,",
            SCREEN_WIDTH / 2 - 520,
            SCREEN_HEIGHT / 2 - 200,
        ),
        TextInfo(
            "so be careful",
            SCREEN_WIDTH / 2 - 280,
            SCREEN_HEIGHT / 2 - 100,
        ),
    ),
)

STAGE5: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (5, 1),
    # platforms
    Group(
        Platform(0, 800, 550, 100),  # floor left side
        Platform(1300, 800, 300, 100),  # floor right side
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(-50, 0, 150, 600),  # left wall
        Platform(1500, 0, 150, 600),  # right wall
        Platform(0, 500, 500, 100),  # left platform
        Platform(700, 700, 150, 200),  # middle platform
        Platform(500, 250, 500, 100),  # upper platform
        Platform(100, 350, 150, 175),  # left upper platform
        Platform(0, 850, 1600, 50),  # long floor
        Platform(1000, 250, 150, 1350),
    ),
    Group(
        # left spike pit
        Spike(550, 800, 50, 50),
        Spike(600, 800, 50, 50),
        Spike(650, 800, 50, 50),
        # right spike pit
        Spike(850, 800, 50, 50),
        Spike(900, 800, 50, 50),
        Spike(950, 800, 50, 50),
        # upper left spikes
        Spike(250, 450, 50, 50),
        Spike(300, 450, 50, 50),
        Spike(1150, 800, 50, 50),
        Spike(1200, 800, 50, 50),
        Spike(1250, 800, 50, 50),
    ),
    None,
    None,
)

STAGE6: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (6, 1),
    # platforms
    Group(
        Platform(0, 800, 400, 100),  # floor
        Platform(600, 800, 300, 100),  # floor
        Platform(1100, 800, 500, 100),  # floor
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(-50, 0, 150, 600),  # left wall
        Platform(1500, 300, 200, 600),  # right wall
        Platform(1100, 0, 150, 600),  # middle wall
        Platform(1450, 600, 150, 50),  # platform lower
        Platform(1150, 500, 150, 50),  # platform middle
        Platform(1450, 400, 150, 50),  # platform upper
    ),
    None,
    Group(
        Lava(400, 850, 200, 75),
        Lava(900, 850, 200, 75),
    ),
    (
        TextInfo(
            'All "bugs" are "intentional" :)',
            SCREEN_WIDTH / 2 - 600,
            SCREEN_HEIGHT - 250,
        ),
    ),
)

STAGE7: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (7, 1),
    # platforms
    Group(
        Platform(0, 700, 300, 200),  # left floor
        Platform(1350, 800, 300, 100),  # right floor
        Platform(0, 0, 400, 100),  # ceiling
        Platform(-50, 300, 150, 600),  # left wall
        Platform(1500, 0, 200, 600),  # right wall
        Platform(1200, 0, 150, 900),  # middle wall
        Platform(550, 550, 150, 150),  # lower platform
        Platform(850, 350, 150, 150),  # middle platform
        Platform(550, 150, 150, 150),  # upper platform
    ),
    None,
    Group(Lava(300, 800, 900, 100)),
    None,
)

STAGE8: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (7, 0),
    # platforms
    Group(
        Platform(0, 0, 1600, 100),  # ceiling
        Platform(-50, 0, 150, 800),  # left wall
        Platform(1500, 0, 200, 900),  # right wall
        Platform(1200, 300, 150, 600),  # middle wall
        Platform(400, 300, 800, 100),  # upper platform
        Platform(100, 450, 100, 100),  # upper box
        Platform(500, 600, 100, 100),  # lower box
        Platform(0, 800, 400, 200),  # floor
    ),
    Group(
        # left spikes
        Spike(550, 250, 50, 50),
        Spike(600, 250, 50, 50),
        Spike(650, 250, 50, 50),
        Spike(700, 250, 50, 50),
        # right spikes
        Spike(1000, 250, 50, 50),
        Spike(1050, 250, 50, 50),
        Spike(1100, 250, 50, 50),
        Spike(1150, 250, 50, 50),
    ),
    None,
    (TextInfo("Dash with SHIFT", SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT - 450),),
)

STAGE9: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (8, 1),
    # platforms
    Group(
        Platform(300, 0, 1300, 100),  # ceiling
        Platform(-50, 0, 150, 600),  # left wall
        Platform(1500, 0, 200, 900),  # right wall
        Platform(500, 600, 350, 100),  # lower dash platform
        Platform(500, 300, 800, 100),  # upper dash platform
        Platform(1100, 600, 400, 100),  # right platform
        Platform(1400, 500, 150, 100),  # right platform elevated ledge
        Platform(50, 300, 150, 100),  # left wall ledge
        Platform(0, 200, 150, 100),
        Platform(0, 800, 300, 200),  # floor
    ),
    Group(
        # bottom spikes
        Spike(650, 550, 50, 50),
        Spike(700, 550, 50, 50),
        Spike(750, 550, 50, 50),
        Spike(800, 550, 50, 50),
        # upper right spikes
        Spike(1000, 250, 50, 50),
        Spike(1050, 250, 50, 50),
        Spike(1100, 250, 50, 50),
        Spike(1150, 250, 50, 50),
        # upper left spikes
        Spike(500, 250, 50, 50),
        Spike(550, 250, 50, 50),
    ),
    Group(Lava(300, 850, 1200, 50)),
    None,
)

STAGE10: Tuple[
    Tuple[int, int], Group, Group | None, Group | None, Tuple[TextInfo, ...] | None
] = (
    # grid location
    (8, 0),
    # platforms
    Group(
        Platform(300, 800, 1300, 100),  # floor
        Platform(-50, 0, 150, 900),  # left wall
        Platform(1500, 0, 200, 900),  # right wall
        Platform(0, 0, 1600, 100),  # ceiling
    ),
    None,
    None,
    (
        TextInfo(
            "you won congrats i guess", SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT / 2 - 50
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
    3: STAGE3,
    4: STAGE4,
    5: STAGE5,
    6: STAGE6,
    7: STAGE7,
    8: STAGE8,
    9: STAGE9,
    10: STAGE10,
}


def grid_to_stage(grid_location: Tuple[int, int]) -> int | str:
    """Returns the corresponding stage number for the grid location.

    :param grid_location: The location of the player on the grid.
    :type grid_location: Tuple[int, int]
    :return: The corresponding stage number.
    :rtype: int | str
    """

    for name, stage in STAGES.items():
        if stage[0] == grid_location:
            return name

    # raise an error if the stage is not found
    raise StageNotFoundError
