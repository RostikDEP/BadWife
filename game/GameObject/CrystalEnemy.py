import pygame
import config
import random

class CrystalEnemy:
	def __init__(self, screen, player):
		self.player = player
		self.screen = screen
		self.size = [48, 57]
		self.image = pygame.image.load("sprites/enemys/crystal.png")
		self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
		self.pos_y = 60
		self.rect = self.surface.get_rect()
		self.position = [110,110]
		self.right = True
		self.right_position =config.SIZE[0] - config.bg_tile_size * 2 - self.size[0]
		self.left_position = config.bg_tile_size * 2
		self.position = [100, 100]
		self.speed = config.speed
		self.canCollide = False


	def Update(self):
		self.UpdatePosition()
		self.surface.fill((0,0,0,0))
		self.surface.blit(pygame.transform.rotate(self.image, 90), (0, 0))
		self.screen.blit(pygame.transform.flip(self.surface, not self.right, 0), self.position)
		self.rect = self.surface.get_rect(topleft=self.position)


	def UpdatePosition(self):
		self.speed = config.speed
		if self.right:
			self.position[0] = self.right_position
		else:
			self.position[0] = self.left_position

		if self.position[1] >= config.SIZE[1]:
			self.position[1] = -self.size[1]
			self.right = self.RandomBool()
		else:
			self.position[1] += self.speed

		if self.rect.colliderect(self.player.rect):
			# pygame.window.set_caption("100")
			if self.canCollide:
				exit()
			self.canCollide = True

	def RandomBool(self):
		if random.randint(0, 100) > 50:
			return False
		else:
			return True

