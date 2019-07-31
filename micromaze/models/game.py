#!/usr/bin/python3.7
# -*-coding:utf-8 -
from.map import Map
from.hero import Hero
from.position import Position

class Game:

    def __init__(self):
        self.map = Map()
        self.map.load_from_file('map/level.txt')
        self.mg = Hero()
        self.map.add_hero(self.mg)
        self.map.add_items.position()# a verifier pour la positon des items sur la map

    def start(self):
        pass

    def move_mg(self):
        pass
    

#Partie de Test du jeu test les passages etc... pour test (python -m micromaze.models.game)
def main():
    game = Game()
    print(game.map.passages)
    
if __name__ == "__main__":
    main()