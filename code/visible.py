import pygame
from settings import *

class Skytile (pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../art/map/skytile.png')
        self.rect = self.image.get_rect(topleft = pos)



