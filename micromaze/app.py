# importation des blibliothèques nècessaires
import pygame as pg

from config import settings
from.models.game import Game
from.controllers.Keyboard import KeyboardController
from.views.map import MapView
from.events import tick #Test les events

class Application:
	#Représente le jeu lui-meme

	

	def __init__(self):
		#Inisialise l'objet pricipale du jeu
		self.game = Game()
		self.keyboard = KeyboardController()
		self.map_view = MapView()
		
		self.running = False
		self.clock = pg.time.Clock()

	def start(self):
		#demarre la boucle du jeu
		self.running = True

		#Boucle principale du jeu
		while self.running:
			self.clock.tick(settings.FPS)
			self.tick_event.send()#Test les events	

def main():
	#point d entree principale du jeu 
	app = Application()
	app.start()


if __name__ == "__main__":
	main()