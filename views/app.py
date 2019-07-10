# importation des blibliothèques nècessaires
import pygame as pg

from config import settings

class Application:
	#Représente le jeu lui-meme

	def __init__(self):
		#Inisialise l'objet pricipale du jeu
		self.running = False
		self.clock = pg.time.Clock()

	def start(self):
		#demarre la boucle du jeu
		self.running = True

		#Boucle principale du jeu
		while self.running:
			pass

def main():
	#point d entree principale du jeu 
	app = Application()
	app.start()


if __name__ == "__main__":
	main()