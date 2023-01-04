import pygame
from settings import *

class Floortile (pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../art/map/floortile.png')
        self.rect = self.image.get_rect(topleft = pos)



