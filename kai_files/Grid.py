import Square
import Constants

class Grid:

	def __init__(self, x_pos, y_pos):
		# use a list to store all components of a grid
		self.square_lst = []

		# create squares
		for row in range(1, 11):
			for col in "ABCDEFGHIJ":
				sq = Square.Square(x_pos, y_pos, (col, row)) # create a new Square object
				self.square_lst.append(sq) # append it to the list of squares
				x_pos += Constants.LENGTH; # set the x_coor for the next row
			x_pos = self.square_lst[0].x_pos # prepare for the next row
			y_pos += Constants.LENGTH


# Grid object tested correct
'''
if __name__ == "__main__":
	grid1 = Grid(100, 100)
	for objs in grid1.square_lst:
		print(objs.x_pos, objs.y_pos, objs.idt)
'''		
