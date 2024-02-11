import pygame


bg_tile_size = 32
SIZE = (360, 600)
FPS = 60
bg_scroll = 0
bg_speed = 3
anim_step = 0
character_height = 68
move_direction = "right"

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Run Game")

tile1 = pygame.image.load("sprites/tiles/tile1.png")
tile2 = pygame.image.load("sprites/tiles/tile2.png")

tile1 = pygame.transform.scale(tile1, (bg_tile_size, bg_tile_size))
tile2 = pygame.transform.scale(tile2, (bg_tile_size, bg_tile_size))

background_lines = pygame.Surface(SIZE)

character = []
for x in range(1, 9):
	character.append(pygame.image.load(f"sprites/character/{x}.png"))

character9 = []
for image in character:
	character9.append(pygame.transform.rotate(image, 90))

background_lines.fill("white")
for x in range(SIZE[1] // bg_tile_size + 1):
	background_lines.blit(tile1, (0, x*bg_tile_size))
	background_lines.blit(tile1, (SIZE[0] - bg_tile_size, x*bg_tile_size))
	background_lines.blit(tile2, (bg_tile_size, x*bg_tile_size))
	background_lines.blit(pygame.transform.flip(tile2, 1, 0), (SIZE[0] - 2*bg_tile_size, x*bg_tile_size))


running = True
while running:
	clock.tick(FPS)

	screen.blit(background_lines, (0, bg_scroll))
	screen.blit(background_lines, (0, -SIZE[1] + bg_scroll))
	if bg_scroll >= SIZE[1]:
		bg_scroll = 0
	else:
		bg_scroll += bg_speed

	if move_direction == "left":
		screen.blit(pygame.transform.flip(character9[anim_step // 5], 1, 0) ,(bg_tile_size * 2, SIZE[1] - 100))
	if move_direction == "right":
		screen.blit(pygame.transform.flip(character9[anim_step // 5], 0, 0) ,(SIZE[0] - bg_tile_size *2 - character_height, SIZE[1] - 100))
	if anim_step >= 7 * 5:
		anim_step = 0
	else:
		anim_step += 1

	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if move_direction == "right":
					move_direction = "left"
				elif move_direction == "left":
					move_direction = "right"
			elif event.key == pygame.K_d:
				print("d")