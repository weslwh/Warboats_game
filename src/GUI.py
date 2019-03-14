import pygame
from math import pi
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#set size
size = [1000,1000]

# set up size for screen
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("War boat")  # set up name

x = 350
y = 0
width = 350
height =350
vel = 5

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    
    for event in pygame.event.get():  #user do something
        if event.type == pygame.QUIT: # if user click close
            done = True
            
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Player screen
    pygame.draw.rect(screen, BLACK, [x, y, width, height], 2)
    # Vertical line for player
    for i in range(1,10):
        pygame.draw.line(screen, BLACK, [x+35*i,y], [x+35*i,height], 2)
    # Horizontal line for player
    for j in range(1,10):
        pygame.draw.line(screen, BLACK, [x,y+35*j], [x+350,y+35*j], 2)

    # Computer screen
    pygame.draw.rect(screen, BLACK, [x, y+450, width, height], 2)

    # Vertical line for computer
    for i in range(1,10):
        pygame.draw.line(screen, BLACK, [x+35*i,y+450], [x+35*i,height+450], 2)
    # Horizontal line for computer
    for j in range(1,10):
        pygame.draw.line(screen, BLACK, [x,y+450+35*j], [x+350,y+450+35*j], 2)
    
    # input the coordinates to board
    Text = ["A","B","C","D","E","F","G","H","I","J"]
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = myfont.render(Text[0], False, (0, 0, 0))
    screen.blit(textsurface,(325,0))

    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = myfont.render(Text[1], False, (0, 0, 0))
    screen.blit(textsurface,(325,35))
    
    pygame.display.flip()
pygame.quit()


