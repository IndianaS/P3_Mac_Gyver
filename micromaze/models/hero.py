#!/usr/bin/python3.7
# -*-coding:utf-8 -
from.map import Map
from.position import right

class Hero:
	
	def __init__(self):
		self.position = None
		self.map = None
		self.loot_items = [] 
	
	def move(self, direction):
		#Calcules la nouvelle position du hero
		new_position = self.position + direction
		if new_position in self.map:
			self.position = new_position
			if self.map.is_exit_position(new_position):
				pass
		        #print ("You are the Best!!!") 
				#if,elif pour valider les trois objets???

	def loot_items(self, item):#Prendre les objets
		pass

class Position:

	def __init__(self,  x, y):
		self.x = x
		self.y = y

	def __eq__(self, position):
		#Determine l'egalité entre la position self et position 
		return self.x == position.x and self.y == position.y

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

#Test position du hero
def main():
    hero = Hero()
    map = Map()
    map.load_from_file('map/level.txt')
    map.add_hero(hero)
    
    print(hero.position)
    hero.move(right)
    hero.move(right)
    hero.move(right)
    hero.move(right)
    print(hero.position)
              

if __name__ == "__main__":
	main()