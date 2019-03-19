import Constants

import pygame
pygame.init()

class Square:

	def __init__(self, x_pos, y_pos, idt):
		# initialize the start_pos and coor of a Square
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.start_pos = (x_pos, y_pos)
		self.idt = idt # e.g. idt = (A, 3) or (H, 5)
		self.check_hit = False
		
		
	def draw_square(self):
		import View # this import has to be in the function, not on top
		# draw the four sides of a square
		pygame.draw.line(View.screen, Constants.BLACK, # Surface, Color
		                 (self.x_pos, self.y_pos), # start point
		                 (self.x_pos + Constants.LENGTH, self.y_pos), # end point
		                 Constants.LINE_WIDTH) # line width = 1
		pygame.draw.line(View.screen, Constants.BLACK,
			         (self.x_pos, self.y_pos),
		                 (self.x_pos, self.y_pos + Constants.LENGTH),
			         Constants.LINE_WIDTH)
		pygame.draw.line(View.screen, Constants.BLACK,
			        (self.x_pos + Constants.LENGTH, self.y_pos),
		                (self.x_pos + Constants.LENGTH, self.y_pos + Constants.LENGTH),
		                Constants.LINE_WIDTH)
		pygame.draw.line(View.screen, Constants.BLACK,
		                (self.x_pos, self.y_pos + Constants.LENGTH),
		                (self.x_pos + Constants.LENGTH, self.y_pos + Constants.LENGTH),
		                Constants.LINE_WIDTH)	
