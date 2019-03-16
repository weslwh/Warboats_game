import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

size = (700, 700)

#initizalize the screen to the given size
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Warboats")

done = False

clock = pygame.time.Clock()


#game loop
HEIGHT = 20
WIDTH = 20
MARGIN = 5
grid = [[0 for x in range(10)] for y in range(10)]

while not done:

    #pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0] // (WIDTH + MARGIN)) + 1
            row = (pos[1] // (HEIGHT + MARGIN)) + 1
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
            
    #Game logic should go here
        
        
    screen.fill(BLACK)
    #pygame.display.flip()
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * (column - 1) + MARGIN,
                                  (MARGIN + HEIGHT) * (row - 1) + MARGIN,
                                  WIDTH,
                                  HEIGHT])        
        
        clock.tick(60)
        pygame.display.flip()
        
        
pygame.quit()       

