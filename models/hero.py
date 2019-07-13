#!/usr/bin/python3.7
# -*-coding:utf-8 -

class Hero:
	
	def __init__(self):
		self.position = None
		self.map = None
		self.item = None #Ou self.positionable = None
	
	def move(self, direction):
		#Calcules la nouvelle position du hero
		new_position = self.position + direction
		if new_position in self.map:
			self.position = new_position

		    if self.map.is_exit_position(position):
				pass
		        #print ("You are the Best!!!") 
				#if,elif pour valider les trois objets???

    def loot_items(self, positionable):#Prendre les objets
		pass              