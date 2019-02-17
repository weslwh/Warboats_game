import Ship


class ShipFactory:
	#The ship factory returns a built ship given the
	#Information the user specifies
	def build(typ, coordinate):
		s = Ship()
		s.set_ship_coordinates(coordinate)
		s.set_type()
		return s
	
	
