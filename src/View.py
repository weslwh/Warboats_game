import Constants
import Grid
import Game_Engine
import time

import pygame
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init() # initialize the pygame module


#get the textready
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 72)
text = font.render('Welcome to Warboats!', False,Constants.BLUE)
font2 = pygame.font.SysFont('Comic Sans MS', 35)
text2 = font2.render('Press C to continue, or Q to quit', False, Constants.BLUE)

#Starts the music playing
pygame.mixer.music.load("game_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#Loop for the start screen
start = False
while not start:
	screen.fill(Constants.WHITE)
	screen.blit(text, (270,200))
	screen.blit(text2, (350, 250))
	
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
				



	pygame.display.update()

	clock.tick(30)
	pygame.display.flip()



pygame.display.update()



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











