import Coordinate.py

class player:
    """

    """
    
    def __init__(self):
        """
        Initializes the player class with a given list of ship objects
        """
        self.ships = []

    def get_ship(self):
        """
        Return the list of ships
        """
        return self.ships

    def guess_position(self, guess: coordinate):
        """
        Return true if guess coordinate matches a ship inside player
        """
        temp = ship()
        temp.set_ship_coordinates(guess)
        
        if (temp in self.ships):
            return True
        
        return False

    def still_has_ship(self):
        """
        Return true if player still has ships
        """
        return self.ships != []

    def add_ships(self, new: Ship):
        """
        Add new to the player ship list.
        Returns false if the coordinates of the new ship overlap with
        an existing ship
        """
        if (new in self.ships()):
            return False
        
        self.ships.append(new)
            
        
