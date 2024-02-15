import pygame
from GameObject import Background
import config

pygame.init()
screen = pygame.display.set_mode(config.SIZE)
pygame.display.set_caption("Run Game")
clock = pygame.time.Clock()

background = Background(screen)

running = True
while running:
	clock.tick(config.FPS)
	pygame.display.update()

	background.Update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
