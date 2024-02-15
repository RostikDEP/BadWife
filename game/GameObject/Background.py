import pygame
import config


class Background:
	def __init__(self, screen):
		self.screen = screen
		self.BackgroundLines = self.BackgroundLines(screen)
		self.surface = pygame.Surface(config.SIZE)
		self.backgroundSpeed = 3
		self.animationStep = 0


	def Update(self):
		self.BackgroundLines.FillLines()
		self.surface.blit(self.BackgroundLines.surface, (0, self.animationStep))
		self.surface.blit(self.BackgroundLines.surface, (0, - config.SIZE[1] +self.animationStep))
		self.screen.blit(self.surface, (0, 0))

		if self.animationStep <= config.SIZE[1]:
			self.animationStep += self.backgroundSpeed
		else:
			self.animationStep = 0


	class BackgroundLines:
		def __init__(self, screen):
			self.surface = pygame.Surface(config.SIZE)
			self.tile_size = config.bg_tile_size
			self.tiles_img = []
			self.tiles = []

			self.LoadTilesImg()
			self.ResizeTiles()
			

		def LoadTilesImg(self):
			self.tiles_img = [
				pygame.image.load("sprites/tiles/tile1.png"),
				pygame.image.load("sprites/tiles/tile2.png")]
			self.tiles = self.tiles_img


		def ResizeTiles(self):
			for i in range(len(self.tiles)):
				self.tiles[i] = pygame.transform.scale(self.tiles[i], (self.tile_size, self.tile_size))


		def FillLines(self):
			self.surface.fill("white")
			for y in range(config.SIZE[1] // self.tile_size + 1):
				self.surface.blit(self.tiles[0], (0, y * self.tile_size))
				self.surface.blit(self.tiles[0], (config.SIZE[0] - self.tile_size, y * self.tile_size))
				self.surface.blit(self.tiles[1], (self.tile_size ,self.tile_size * y))
				self.surface.blit(pygame.transform.flip(self.tiles[1], 1, 0), (config.SIZE[0] - 2*self.tile_size, y * self.tile_size))