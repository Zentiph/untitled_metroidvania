"""Stages.stages.py

Module containing all the preset stages for the game.
"""

from typing import Dict, Union

from ..Internal import SCREEN_HEIGHT, SCREEN_WIDTH
from ..Level import Group, Platform, Spike

_TEST: Group = Group(
    # platforms
    Platform(0, SCREEN_HEIGHT, SCREEN_WIDTH, 50)
)

_STAGE_1: Group = Group(
    # platforms
    Platform(0, 850, 1600, 50),  # floor
    Platform(0, 0, 1600, 50),  # ceiling
    Platform(0, 0, 50, 450),  # left wall
    Platform(0, 800, 50, 100),  # botton ledge
    Platform(0, 450, 50, 350, False, (255, 255, 255)),  # walkable wall
    Platform(500, 800, 100, 100),
    Platform(1000, 800, 100, 100),
    # hazards
    Spike(600, 825, 400, 25),
)

STAGES: Dict[Union[int, str], Group] = {
    "test": _TEST,
    1: _STAGE_1,
}
