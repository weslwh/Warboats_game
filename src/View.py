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

MARGIN = 5

grid = []
grid2 = []
for row in range(10):

    grid.append([])
    grid2.append([])
    for column in range(10):
        grid[row].append(0)  
        grid2[row].append(0)

pygame.init()
font = pygame.font.Font(None, 25)
WINDOW_SIZE = [720, 600]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Warboats")

done = False
 
clock = pygame.time.Clock()

framecount = 0
framerate = 60
lasttime = 0
minutes = 0
seconds = 0
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // ((HEIGHT + MARGIN))
            row = pos[1] // ((HEIGHT + MARGIN))
            if (pos[1] > 250):
                row = row - 12  
                grid2[row][column] = 1
                
            elif (pos[1] < 250):
                grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    screen.fill(BLACK)

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
    time = pygame.time.get_ticks

    #This code gets the time and prints it
    totalseconds = framecount // framerate
    minutes  = totalseconds // 60
    seconds = totalseconds % 60
    framecount += 1
    outputs = "Time: {0:02}:{1:02}".format(minutes, seconds)
    text = font.render(outputs, True, WHITE)
    screen.blit(text, [250, 250])
 
    if (lasttime != seconds):
        print(totalseconds)
        print(minutes)
        lasttime = seconds
    clock.tick(60)





    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()