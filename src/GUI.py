import pygame
import sys
import time
from math import pi

# Initialize pygame
pygame.init()

# Define colors
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

# width and height of each grid and gap bewteen each grid
width = 25
height = 25
gap = 5

# total width and total height
total_width = 250
total_height = 250

# make a 10*10 grids
# initialize original position to be 0, if no ship there.
grid = []
for x in range(0,10):
    grid.append([])
    for y in range(0,10):
        grid[x].append(0)

#  Initialize the screen size 
Screen_width = 1000
Screen_height = 1000
# Make the screen
Screen = pygame.display.set_mode([Screen_width,Screen_height])

# Set title name
pygame.display.set_caption("Warboats")
guess_coordinate = []
color = WHITE
### guess board
##for x in range(0,10):
##    for y in range(0,10):
##        pygame.draw.rect(Screen,color, [(width+gap)*x+gap,(height+gap)*y+gap,width,height])
##

# guess board
for x in range(0,10):
    for y in range(0,10):
        pygame.draw.rect(Screen,color, [(width+gap)*x+gap,(height+gap)*y+gap,width,height])
# place ship board
for x in range(0,10):
    for y in range(0,10):
        pygame.draw.rect(Screen,color, [(width+gap)*x+gap,(height+gap)*y+gap+350,width,height])


# Close the screen
Exit = False
clock = pygame.time.Clock()
while not Exit:
    clock.tick(10)

    for event in pygame.event.get():  #user do something
        if event.type == pygame.QUIT: # if user click close
            pygame.quit() # quit pygame 
            sys.exit() # system exit
            Exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            p_x,p_y = pygame.mouse.get_pos() # get the position of x coordinate ,y coordinate
            if p_x <=300 and p_y <=300: # limit the guess board
                x_value = p_x//((height+gap)) # 
                y_value = p_y//((height+gap))
                guess_coordinate.append((x_value+1,y_value+1)) # add all guess_coordinate as tuple into guess_coordinate list
            print(guess_coordinate)

                




    # update screen to get the draw 
    pygame.display.flip()
pygame.quit()











        
            
