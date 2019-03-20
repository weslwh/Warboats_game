import Square
import Constants

class Grid:

	def __init__(self, x_pos, y_pos):
		# use a list to store all components of a grid
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.square_lst = []

		# create squares
		for row in range(1, 11):
			for col in "ABCDEFGHIJ":
				sq = Square.Square(x_pos, y_pos, (col, row)) # create a new Square object
				self.square_lst.append(sq) # append it to the list of squares
				x_pos += Constants.LENGTH; # set the x_coor for the next row
			x_pos = self.square_lst[0].x_pos # prepare for the next row
			y_pos += Constants.LENGTH


	def draw_grid(self):
		for obj in self.square_lst:
			obj.draw_square()
			
	def draw_index(self):
		import View
		import pygame
		pygame.init()
		
		# set the font of the letters
		font = pygame.font.SysFont("arial", 25)
		
		# make local variables for horizontal indices
		h1_pos = self.x_pos + 9
		v1_pos = self.y_pos - 35
		
		# render text
		for letter in "ABCDEFGHIJ":
			label = font.render(letter, 1, (0, 0, 128))
			View.screen.blit(label, (h1_pos, v1_pos))
			pygame.display.flip()
			h1_pos += Constants.LENGTH
			
		# make local variables for vertical indices
		h2_pos = self.x_pos - 30
		v2_pos = self.y_pos + 3
			
		# render text
		for num in range(1, 11):
			label = font.render(str(num), 1, (0, 0, 128))
			View.screen.blit(label, (h2_pos, v2_pos))
			pygame.display.flip()
			v2_pos += Constants.LENGTH