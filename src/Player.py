
class Player:
    """
    initilize the player in the Warboats game.

    Methods:
        __init__(self)
        add_ships(self, new_ship)
        get_ship(self)
        guess_position(self, guess_coordinate)
        still_has_ship(self)
    """
    
    def __init__(self):
        """
        Initializes the player class with a given list of ship objects

        Args:
            void

        Returns:
            void

        Raises:
            void
        """
        self.ships = []

    def add_ships(self, new_ship):
        """
        Add ship to the player ship list.
        Returns false if the coordinates of the new ship overlap with
        an existing ship

        Args:
            new_ship(Ship): Ship

        Returns:
            void

        Raises:
            void
        """
        if (new in self.ships()):
            return False
        
        self.ships.append(new)

    def get_ship(self):
        """
        Return the list of ships

        Args:
            void

        Returns:
            List[Ship]: return list of ships for self object

        Raises:
            void
        """
        return self.ships

    def guess_ship_position(self, coordinate):
        """
        Return true if guess coordinate matches a ship inside player
        
        Args:
            coordinate(): The Coordinate to be guessed

        Returns:
            Boolean(): return True if the coordinate is part of the ships

        Raises:
            void
        
        """
        temp = ship()
        temp.set_ship_coordinates(guess)
        
        if (temp in self.ships):
            return True
        
        return False

    def still_has_ship(self):
        """
        Return true if player still has ships
        
        Args:
            void

        Returns:
            Boolean(): return true if player has ship

        Raises:
            void
        """
        return self.ships != []


            
        
