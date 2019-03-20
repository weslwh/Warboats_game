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

#initializes variables
pos = [0,0]
grid = [[0],[0]]
grid2 = [[0],[0]]
row = 0
column = 0
HEIGHT = 30
MARGIN = 3

# while-loop logic
while not Constants.GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Constants.GAME_OVER = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // ((HEIGHT + MARGIN))
                row = pos[1] // ((HEIGHT + MARGIN))
                valid_click = 0

                if (pos[1] > 250 and pos[0] < 250):
                    valid_click = 1
                    row = row - 12  
                    grid2[row][column] = 1
                    last_column = column
                    last_row = row

                elif (pos[1] < 250 and pos[0] < 250):
                    valid_click = 1
                    grid[row][column] = 1
                    last_column = column
                    last_row = row
                else:
                    valid_click = 0
                print("Click ", pos, "Grid coordinates: ", row, column)
			                
                        
pygame.quit()
