import pygame
import sys

#Framarate of the game
FPS = 60

#The size of the tiles
TILE_SIZE = 64

WORLD_MAP = [
['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
['-','1','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','2','-'],
['f','f','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
['f','f','f','f','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],
['f','f','f','f','f','f','-','-','-','-','-','-','-','-','-','-','-','-','-','-','f','-','-','f'],
['f','f','f','f','f','f','f','f','-','-','-','-','-','-','-','-','-','-','f','f','f','-','-','f'],
['f','f','f','f','f','f','f','f','f','f','-','-','-','-','-','-','f','f','f','f','f','-','-','f'],
['f','f','f','f','f','f','f','f','f','f','f','f','-','-','-','-','-','-','-','-','-','-','-','f'],
['f','f','f','f','f','f','f','f','f','f','f','f','f','f','-','-','-','-','-','-','-','-','-','f'],
['f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f'],
['f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f','f'],
]

#The amount of tiles a game window will have, width first, height second.
GAME_SIZE = [24, 14]

#Resolution of the game window being calculated from the tile size and game size
WIDTH = GAME_SIZE[0] * TILE_SIZE
HEIGHT = GAME_SIZE[1] * TILE_SIZE
SCREEN_SIZE = (WIDTH, HEIGHT)