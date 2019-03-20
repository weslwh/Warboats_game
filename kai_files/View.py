import Constants
import Square
import Grid
import pygame
pygame.init()

# initialize the screen, background, and caption
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
screen.fill(Constants.PALE_TURQUOISE)
pygame.display.set_caption(Constants.CAPTION)

# update the screen
pygame.display.flip()

'''
# tests for draw_square correct
sq1 = Square.Square(100, 100, 0)
sq1.draw_square()
'''



# initialize the coordinates
player_grid = Grid.Grid(100, 100)
player_grid.draw_grid()
player_grid.draw_index()

oppo_grid = Grid.Grid(600, 100)
oppo_grid.draw_grid()
oppo_grid.draw_index()
	
pygame.display.flip()

# while-loop logic
while not Constants.GAME_OVER:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Constants.GAME_OVER = True
