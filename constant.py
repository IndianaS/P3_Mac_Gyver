#!/usr/bin/python3.5
# -*-coding:utf-8 -
"""Place where constants are"""

import pygame
from pygame.locals import *

pygame.init()

#Dimensions of game window
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NB_SPRITE + 2) * SPRITE_SIZE, (NB_SPRITE + 2) * SPRITE_SIZE)

#Display video of window game
window = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "help MacGyver!!"

#Screen (home)
HOME = pygame.image.load("pictures/home.png").convert()

#Screen (Welcome to the game)
WELCOME = pygame.image.load("pictures/welcome.png").convert_alpha()

#Screen (Game-Over)
GAMEOVER = pygame.image.load("pictures/game_over.png").convert_alpha()