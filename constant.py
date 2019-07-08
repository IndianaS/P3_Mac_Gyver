#!/usr/bin/python3.7
# -*-coding:utf-8 -
"""Place where constants are"""

import pygame
from pygame.locals import *

pygame.init()

#Dimensions of game window
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NB_SPRITE + 2) * SPRITE_SIZE, (NB_SPRITE + 2) * SPRITE_SIZE)

VELOCITY = 10 #PX

#Display video of window game
window = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "help MacGyver!!"

#Screen (home)
HOME = pygame.image.load("pictures/home.png").convert()

#Screen (Welcome to the game)
WELCOME = pygame.image.load("pictures/welcome.png").convert_alpha()

#Screen (Game-Over)
GAMEOVER = pygame.image.load("pictures/game_over.png").convert_alpha()

#Screen (You win)
WIN = pygame.image.load("pictures/win.png").convert_alpha()

#Game background
BACKGROUND = pygame.image.load("pictures/background.jpg").convert()

#kind of sprite
WALL = pygame.image.load("pictures/wall.png").convert_alpha()
EXIT = pygame.image.load("pictures/guardian.png").convert_alpha()

#kind of tools
TUBE = pygame.image.load("pictures/tube.png").convert_alpha()
ETHER = pygame.image.load("pictures/ether.png").convert_alpha()
SYRINGE = pygame.image.load("pictures/syringe.png").convert_alpha()

#Display MacGyver
MG = pygame.image.load("pictures/MacGyver.png").convert_alpha()

#map skeleton
START_CHAR = 'd'
PASSAGE_CHAR = '0'
WALL_CHAR = 'w'
EXIT_CHAR = 'a'

#map variable
FILE = "map/level1.txt"