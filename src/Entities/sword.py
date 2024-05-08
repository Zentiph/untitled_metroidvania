import pygame
from pygame.sprite import _Group
from ..Entities import player

class sword(pygame.sprite.Sprite):
    '''sword that swings and attacks enemies'''

    def __init__(self)