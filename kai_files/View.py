import Constants
import Square
import Grid
import pygame
pygame.init()

# initialize the screen, background, and caption
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
screen.fill(Constants.PALE_TURQUOISE)
pygame.display.set_caption(Constants.CAPTION)


# initialize the coordinates
player_grid = Grid.Grid(100, 100)
player_grid.initialize()

oppo_grid = Grid.Grid(600, 100)
oppo_grid.initialize()

pygame.display.flip()

# while-loop logic
while not Constants.GAME_OVER:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Constants.GAME_OVER = True
