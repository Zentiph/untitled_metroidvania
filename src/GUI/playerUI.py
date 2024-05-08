"""playerUI

playerUI contains various functions used the creation and utilization of graphical aspects that are visible at all times outside of menus.
"""

from pygame import Rect, draw, display

def healthBar_create(inputSurface, xPos, yPos):
    draw.rect(inputSurface, (255,0,0), Rect(xPos, yPos, 200, 30))
    display.flip()

class healthBar:
    def __init__(
        draw.rect(inputSurface, (255,0,0), Rect(xPos, yPos, 200, 30))
        display.flip()
    ) -> None:0
        

# learn classes
# init is "on start, do" and sets custom vars just like parameters for a function
# make healthbar appear in bottom left
# make health bar green% = %health