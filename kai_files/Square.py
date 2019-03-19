import Constants

class Square:

	def __init__(self, x_pos, y_pos, idt):
		# initialize the start_pos and coor of a Square
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.start_pos = (x_pos, y_pos)
		self.idt = idt # e.g. idt = (A, 3) or (H, 5)
		self.check_hit = False
