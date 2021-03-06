import pygame
import Constants
import Square
import Grid
import Game_Engine
pygame.init()
class Ship(pygame.sprite.Sprite):
    
    """
    Represents a ship object, which has a list of Coordinates that 
    represent it's position and a Boolean 'sunk' attribute representing
    if the ship has been sunk in the Warboats game.
    
    Methods:
        __init__(self)
        get_ship_coordinates(self)
        guess_position(self, pos)
        set_ship_coordinate(self, pos)
        is_sunk(self)
    """
    
    def __init__(self, x_pos, y_pos, ship_size):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ship_size = ship_size
        
        """
        Initializes a ship object with no coordinates.
        
        Args:
            void
        
        Returns:
            void
        
        Raises:
            void
        """
        self.position = []
        self.sunk = False
        self.type = ""
        

    def get_ship_coordinates(self):
        """
        Return the list of coordinates that comprise this ship's 
        location.
        
        Args:
            void
        
        Returns:
            coords (List[Coordinate]): The coordinates that represent this ship's position
        
        Raises:
            void
        """
         

    
    
      
    def guess_position(self, pos):
        """
        Guesses a position against this Ship, returns true if the
        coordinate guessed is a coordinate comprisiing the ship's
        position.
        
        Args:
        pos (Coordinate): The coordinate to be guessed.
        
        Returns:
            is_coordinate (Boolean): True if pos is in this ship's position
        
        Raises:
            void
        """
        for i in position:
            if i == pos:
                return True
        
        return False
    

    def set_ship_coordinates(self, pos):
        """
        Set this ship's coordinates to be the coordinates in pos
        
        Args:
            pos (List[Coordinate): the list of coordinates to comprise this ship's position
        
        Returns:
            void
        
        Raises:
            void
        """
        self.position = pos

    def set_type(self, ship_type):
        """
        Changes the ship's object type into one of four types:
        - Battleship
        - Cruiser
        - Frigate
        - Minesweeper

        Args:
            ship_type (String): The type of ship to be set to

        Returns:
            void
        """

        self.type = ship_type
        

    def is_sunk(self):
        """
        Return True if this ship has been sunk.
        
        Args:
            void
        
        Returns:
            is_sunk (Boolean): True if this ship is sunk
        
        Raises:
            void
        """
        return self.sunk
        
