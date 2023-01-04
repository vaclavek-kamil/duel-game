import pygame
from settings import *
from visible import *
from obstacles import *
from players import *

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):

                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == 'f':
                    Floortile((x,y), [self.obstacles_sprites])

                if col == '-':
                    Skytile((x,y), [self.visible_sprites])

                if col == '1':
                    Player1((x,y), [self.players])
                    Skytile((x,y), [self.visible_sprites])

                if col == '2':
                    Player2((x,y), [self.players])
                    Skytile((x,y), [self.visible_sprites])

    def run(self):
        #update and draw the game
        self.obstacles_sprites.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)
        self.players.draw(self.display_surface)