import pygame
import config


class CrystalEnemy:
	def __init__(self, screen, player):
		self.player = player
		self.screen = screen
		self.size = [48, 57]
		self.image = pygame.image.load("sprites/enemys/crystal.png")
		self.surface = pygame.Surface(self.size)
		self.pos_y = 60
		self.rect = self.surface.get_rect()
		self.position = [110,110]
		self.right = False
		self.right_position =config.SIZE[0] - config.bg_tile_size * 2 - self.size[0]
		self.left_position = config.bg_tile_size * 2
		self.position = [self.right_position, 0]


	def Update(self):
		self.surface.blit(pygame.transform.flip(pygame.transform.rotate(self.image, 90), not self.right	, 0), (0, 0))
		self.screen.blit(self.surface, self.position)
		self.rect = self.surface.get_rect(topleft=self.position)

		# if self.rect.colliderect(self.player.rect):
		# 	exit()