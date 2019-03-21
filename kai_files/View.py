import Constants
import Grid
import Game_Engine

import pygame
pygame.init() # initialize the pygame module




# initialize the screen, background and caption
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
screen.fill(Constants.PALE_TURQUOISE)
pygame.display.set_caption(Constants.CAPTION)





# initialize the two coordinates and index
player_grid = Grid.Grid(100, 100) # create a View object
player_grid.initialize() # create a View object
oppo_grid = Grid.Grid(600, 100)
oppo_grid.initialize()

# update the screen
pygame.display.update()





# start the game
Game_Engine.start()

pygame.quit()











