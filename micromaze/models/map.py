#!/usr/bin/python3.7
# -*-coding:utf-8 -
from config import settings
from.position import Position

class Map:
	

	def __init__(self):
		self.start = None
		self.exit = None
		self.passages = []
		self.wall = []
		self.items = []
		self.hero = None
		self.width = None
		self.height = None
	
	def load_from_file(self, filename):
    	#charge le contenu du fichier filename dans les listes
		with open(filename) as level:
			for n_line, line in enumerate(level):
				for n_char, char in enumerate(line):
					position = Position(n_char, n_line)
					if char == settings.START_CHAR:
						self.passages.append(position)
						self.start = position
					elif char == settings.EXIT_CHAR:
						self.passages.append(position)
						self.exit = position
					elif char == settings.PASSAGE_CHAR:
						self.passages.append(position)
					else:
						self.wall.append(position)

			self.height = n_line + 1
			self.width = n_char + 1



	def add_hero(self, hero):
    	#Positionne le hero sur la Map
		self.hero = hero
		self.hero.position = self.start
		self.hero.map = self


	def __contains__(self, position):
		return position in self.passages
    

	def is_exit_position(self, position):
		return position == self.exit