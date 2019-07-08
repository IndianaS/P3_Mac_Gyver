#!/usr/bin/python3.7
# -*-coding:utf-8 -

import pygame

class Hero:
	
	def __init__(self):
		self.position = None
		self.map = None
	
	def move(self, direction):
		#Calcules la nouvelle position du hero
		new_position = self.position + direction
		if new_position in self.map:
			self.position = new_position

		if 
				
