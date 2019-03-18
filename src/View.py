"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
grid2 = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    grid2.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
        grid2[row].append(0)
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [720, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Warboats")

done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // ((HEIGHT + MARGIN))
            row = pos[1] // ((HEIGHT + MARGIN))
            # Set that location to one
            if (pos[1] > 250):

                row = row - 12
                
                grid2[row][column] = 1
            elif (pos[1] < 250):

                grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
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
        
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()