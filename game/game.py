import pygame
from GameObject import Background, Player
import config

pygame.init()
screen = pygame.display.set_mode(config.SIZE)
pygame.display.set_caption("Run Game")
clock = pygame.time.Clock()

background = Background(screen)
player = Player(screen)

running = True
while running:
	events = pygame.event.get()
	clock.tick(config.FPS)
	pygame.display.update()

	background.Update()
	player.Update(events)

	for event in events:
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()