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
		import View
		
		pygame.draw.rect(View.screen, Constants.BLACK, (self.x_pos, self.y_pos,
		                Constants.LENGTH, Constants.LENGTH), Constants.LINE_WIDTH)
		
	def fill_square(self):
		import View
		
		pygame.draw.rect(View.screen, Constants.KHAKI, (self.x_pos + 2, self.y_pos + 2,
			        Constants.LENGTH - 4, Constants.LENGTH - 4), 0)		
		
		pygame.display.update()
