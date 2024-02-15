import pygame
import config

class Player:
	def __init__(self, screen):
		self.screen = screen
		self.size = (68, 46)
		self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
		self.src_images = []
		self.images = []
		self.image = None
		self.position = [0, 0] 
		self.bottom_spase = 100
		self.direction = True
		self.animate_step = 0
		self.animate_speed = 5
		self.animate_step_limit = 8 * self.animate_speed
		self.right_position = (config.SIZE[0] - config.bg_tile_size * 2 - self.size[0], config.SIZE[1] - self.bottom_spase)
		self.left_position = (config.bg_tile_size * 2, config.SIZE[1] - self.bottom_spase)

		self.LoadImg()
		self.rect = self.surface.get_rect()


	def LoadImg(self):
		for i in range(1, 9):
			self.src_images.append(pygame.transform.rotate(pygame.image.load(f"sprites/character/{i}.png"), 90))


	def Update(self, events):
		self.events = events
		self.UpdatePosition()
		self.Render()


	def Render(self):
		self.surface.blit(self.src_images[0], (0, 0))
		self.surface = pygame.transform.flip(self.surface, not self.direction, 0)
		self.screen.blit(self.surface, self.position)


	def UpdatePosition(self):
		if self.direction:
			self.position = self.right_position
		else:
			self.position = self.left_position

		for event in self.events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.direction = not self.direction