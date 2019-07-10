import pygame

from config import settings

class HeroSprite(pg.sprite.Sprite):

	def __init__(self):
		self.image = pg.image.load(settings.MG).convert_alpha()
		self.rect = self.image.get_rect()

	def update(self):
		

