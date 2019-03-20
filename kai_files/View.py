import Constants
import Square
import Grid
import pygame
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

pygame.display.flip()
pygame.font.init()
#initializes variables
pos = [0,0]
grid = [[0,0],[0,0]]
grid2 = [[0,0],[0,0]]
row = 0
column = 0
HEIGHT = 30
WIDTH = 30
MARGIN = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
KHAKI = (240, 230, 140)
PALE_TURQUOISE = (175, 238, 238)



#get the textready
font = pygame.font.SysFont('Comic Sans MS', 30)
text = font.render('Welcome to Warboats!', False,Constants.BLUE)
font2 = pygame.font.SysFont('Comic Sans MS', 15)
text2 = font2.render('Press C to continue, or Q to quit', False, Constants.BLUE)

start = False
while not start:
	screen.fill(Constants.WHITE)
	screen.blit(text, (350,200))
	screen.blit(text2, (380, 250))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			start = True
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:		
			if event.key == pygame.K_q:
				start = True
				pygame.quit()
				quit()
			if event.key == pygame.K_c:
				start = True
				print(start)
				

	if start == True:
		print("here")
		
	pygame.display.update()

	clock.tick(30)
	pygame.display.flip()
	
	

pygame.display.update()
print("I GOT HERE")














# while-loop logic
#Still need to properly transfer the code from other View.py and update it to this version
while not Constants.GAME_OVER:
        valid_click=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Constants.GAME_OVER = True
                    pygame.quit()

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

        screen.fill(BLACK) #May not need this
        if valid_click == 1:
            for row in range(10):
                for column in range(10):
                    color = WHITE
                    pygame.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
                    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN+ 300,WIDTH, HEIGHT])
                    if grid[row][column] == 1:
                        color = GREEN
                        pygame.draw.rect(screen,color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])
                    elif grid2[row][column] == 1:
                        color = GREEN
                        pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN+ 300,WIDTH, HEIGHT])
                    pygame.draw.rect(screen, RED, (0,252, 250, 50), 0)

        else:
            for last_row in range(10):
                for last_column in range(10):
                    color = WHITE
                    pygame.draw.rect(screen,color, [(MARGIN + WIDTH) * last_column + MARGIN, (MARGIN + HEIGHT) * last_row + MARGIN,WIDTH, HEIGHT])
                    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * last_column + MARGIN, (MARGIN + HEIGHT) * last_row + MARGIN+ 300,WIDTH, HEIGHT])
                    if grid[last_row][last_column] == 1:
                        color = GREEN
                        pygame.draw.rect(screen,color, [(MARGIN + WIDTH) * last_column + MARGIN, (MARGIN + HEIGHT) * last_row + MARGIN,WIDTH, HEIGHT])
                    elif grid2[last_row][last_column] == 1:
                        color = GREEN
                        pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * last_column + MARGIN, (MARGIN + HEIGHT) * last_row + MARGIN+ 300,WIDTH, HEIGHT])
                    pygame.draw.rect(screen, RED, (0,252, 250, 50), 0) 
                        
pygame.quit()
