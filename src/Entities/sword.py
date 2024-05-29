import pygame
from pygame.sprite import _Group
from ..Entities import Player



def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

class sword(pygame.sprite.Sprite):
    '''sword that swings and attacks enemies'''

    def __init__(self):
        pygame.sprite.Sprite(self)
        self.image, self.rect = load_png("src\Media\Images\Sprites\Player\sword.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed= 10
        s
    def sword_swing_up(self):
       Player.coords
       
       pygame.draw.rect()
        
