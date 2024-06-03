"""Stages.stages.py

Module containing all the preset stages for the game.
"""

from typing import Dict, List, Union

from ..Internal import SCREEN_HEIGHT, SCREEN_WIDTH
from ..Level import Group, Platform, Spike

__all__ = ["STAGES", "_TEST", "_STAGE1"]

_TEST: List[Group] = [
    # platforms
    Group(Platform(0, SCREEN_HEIGHT, SCREEN_WIDTH, 50))
]

_STAGE1: List[Group] = [
    # platforms
    Group(
        Platform(0, 850, 1600, 50),  # floor
        Platform(0, 0, 1600, 50),  # ceiling
        Platform(0, 0, 50, 450),  # left wall
        Platform(0, 800, 50, 100),  # bottom ledge
        Platform(0, 450, 50, 350, False, (255, 255, 255)),  # walkable wall
    )
]

_STAGE2: List[Group] = [
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
    Group(Spike(600, 825, 400, 25)),
]

STAGES: Dict[Union[int, str], List[Group]] = {"test": _TEST, 1: _STAGE1, 2: _STAGE2}
