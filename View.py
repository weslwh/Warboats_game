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
while not done:
    
    grid = [[0 for x in range(10)] for y in range(10)]

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("yoube pushed a button")
            
        #Game logic should go here
        
        
        screen.fill(WHITE)
        #pygame.display.flip()
        
        clock.tick(60)
        
        
        
pygame.quit()       

