#!/usr/bin/python3.7
# -*-coding:utf-8 -
from.map import Map

class Items:
    def __init__(self, position):
        self.position = position



#Test Items position
tube = Items(test_map.random_position[0])
syringe = Items(test_map.random_position[1])
ether = Items(test_map.random_position[2])

print(tube.position)
