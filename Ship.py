import Coordinate.py

class Ship:
    """
    An object representation of a ship
    """
    
    def __init__(self):
        """
        Initializes ship class
        """
        self.position = []
        self.sunk = False

    def get_ship_coordinates(self):
        """
        Return the list of ships
        """
        return self.position
      
    def guess_position(self, pos: Coordinate):
        """
        Returns true if pos matches the ship's coordinates
        """
        for i in position:
            if i = pos:
                return True
        
        return False

    def set_ship_coordinates(self, pos: Coordinate):
        """
        Changes ship position with new coordinate, pos
        """
        self.position = pos

    def is_sunk(self):
        """
        Return true if sunk is true for ship
        """
        return self.sunk
        
