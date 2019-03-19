import Constants
import pygame
pygame.init()

# initialize the screen, background, and caption
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
screen.fill(Constants.WHITE)
pygame.display.set_caption(Constants.CAPTION)

# update the screen
pygame.display.flip()

# initialize the coordinates
pygame.draw.line(screen, Constants.BLACK, (50, 50), (100, 100), 3)
pygame.display.flip()

# while-loop logic
while not Constants.GAME_OVER:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Constants.GAME_OVER = True
