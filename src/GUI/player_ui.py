"""GUI.player_ui.py

player_ui contains various functions used for the creation
and utilization of graphical aspects that are visible at
all times outside of menus.
"""

from pygame import Rect, draw, display


class HealthBar:
    def __init__(self, frame, xcor, ycor):
        draw.rect(frame, (255, 0, 0), Rect(xcor, ycor, 200, 30))
        display.flip()


# learn classes
# init is "on start, do" and sets custom vars just like parameters for a function
# make healthbar appear in bottom left
# make health bar green% = %health
