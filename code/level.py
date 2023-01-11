import pygame
from settings import *
from visible import *
from obstacles import *
from players import *

class Level:
    def __init__(self):
        #getting the display surface from the library
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()
        self.pressed_keys = pygame.key.get_pressed()


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
                    self.player1 = Player1((x,y))
                    Skytile((x,y), [self.visible_sprites])

                if col == '2':
                    self.player2 = Player2((x,y))
                    Skytile((x,y), [self.visible_sprites])

    def run(self):
        #get the keyboard status, which will be used across all the update functions
        self.pressed_keys = pygame.key.get_pressed()

        #update tye game objects
        self.player1.update(self)
        self.player2.update(self)

        #draw the game objects 
        self.obstacles_sprites.draw(self.display_surface)
        self.visible_sprites.draw(self.display_surface)

        self.player1.custom_draw(self)
        self.player2.custom_draw(self)
