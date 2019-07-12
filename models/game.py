#!/usr/bin/python3.7
# -*-coding:utf-8 -
from.map import Map

class Game:

    def __init__(self):
        self.map = Map()
        self.map.load_from_file('map/level.txt')
        self.mg = None

    def start(self):
        pass

    def move_mg(self):
        pass




#Test Game
def main():
    game = Game()
    print(game.map.passages)

if __name__ == '__main__':
        main()

