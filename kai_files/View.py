import Constants
import Square
import Grid
import pygame
import Game_Engine
pygame.init()


# initialize the screen, background, and caption
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
screen.fill(Constants.PALE_TURQUOISE)
pygame.display.set_caption(Constants.CAPTION)
clock = pygame.time.Clock()

# initialize the coordinates
player_grid = Grid.Grid(100, 100)
player_grid.initialize()

oppo_grid = Grid.Grid(600, 100)
oppo_grid.initialize()

# update the screen
pygame.display.flip()

# while-loop logic
while not Constants.GAME_OVER:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Constants.GAME_OVER = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            # Simply prints messages, modifications expected.
            Game_Engine.get_click_info(x, y)
            
            # Fill the square
            Game_Engine.fill_square(x, y)


pygame.quit()