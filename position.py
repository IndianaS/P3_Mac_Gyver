#!/usr/bin/python3.7
# -*-coding:utf-8 -


class Position:

	def __init__(self,  x, y):
		self.x = x
		self.y = y

	def __eq__(self, position):
		#Determine l'egalité entre la position self et position 
		return self.x, self.y == position.x, position.y

	def __add__(self, motion):
		#Ajoute le deplacement motion a la position self.
		return Position(self.x + motion.dx, self.y + motion.dy)


class Motion:

	def __init__(self, dx, dy):
		self.dx = dx
		self.dy = dy

up = Motion(0, -1)
down = Motion(0, 1)
left = Motion(-1, 0)
right = Motion(1, 0)
