#!/usr/bin/python3.7
# -*-coding:utf-8 -





class Map():
	#class object Map which define the labyrinth.
    #It has one attribut : an empty grid.
    #and takes as parameter the file.txt which contains the map.
    #This class has two methods: one to generate the structure : a list of list
    #and one to display the grid over the pygame window.

    def __init__(self, file):
    	self.file = file
    	self.grid = []

    def generate(self):
    	frame = []