import pygame
from settings import *

class Player1 (pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../art/player/p1-idle.png')
        self.rect = self.image.get_rect(topleft = pos)

class Player2 (pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../art/player/p2-idle.png')
        self.rect = self.image.get_rect(topleft = pos)


