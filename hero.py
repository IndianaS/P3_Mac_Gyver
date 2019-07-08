#!/usr/bin/python3.7
# -*-coding:utf-8 -

class Hero:
	
	def __init__(self):
		self.position = None
		self.map = None
	
	def move(self, direction):
		#Calcules la nouvelle position du hero
		new_position = self.position + direction
		if new_position in self.map:
			self.position = new_position

		    if self.map.is_exit_position(position):
		        #print ("You are the Best!!!") 
				#if,elif pour valider les trois objets???
