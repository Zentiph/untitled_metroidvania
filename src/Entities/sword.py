import pygame
from pygame.sprite import _Group
from ..Entities import Player
from ..Internal import load_png
from 


class sword(pygame.sprite.Sprite):
    '''sword that swings and attacks enemies'''

    def __init__(self):
        pygame.sprite.Sprite(self)
        self.image, self.rect = load_png("src\Media\Images\Sprites\Player\sword.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed= 10

    def sword_swing_up(self):
       playe
       pygame.draw.rect()
        
