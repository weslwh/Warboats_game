class Coordinate:
    """
    The Coordinate class is used to represent a position on 
    the game board for the Warboats game.
    
    Methods:
        __init__(self, lettercord, numbercord)
        get_letter()
        get_number()
        get_array()
    """
    
    def __init__(self, lettercoord, numbercoord):
        """
        Initialize a Coordinate object with the corresponding
        letter and number values provided as arguments.
        
        E.g. "A1", "B5", etc.
        
        Args:
            lettercoord (String): The respective letter.
            numbercoord (int): The respective number.
        
        Returns:
            void
        
        Raises:
            void
        """
        self.lettercoord = lettercoord
        self.numbercoord = numbercoord
        
    
    def get_letter(self):
        """
        Return the corresponding letter of this Coordinate.
        
        Args:
            void
        
        Returns:
            letter (String): The respective letter of this Coordinate.
        
        Raises:
            void
        """
        return self.lettercoord
    
    
    def get_number(self):
        """
        Return the corresponding number of this Coordinate.
        
        Args:
            void
        
        Returns:
            number (int): The respective number of this Coordinate.
        
        Raises:
            void
        """
        return self.numbercoord
    

    def get_tuple(self):
        """
        Return a tuple representation of this Coordinate.
        
        Args:
        void
        
        Returns:
        tuple_representation (tuple): Where the first element is the letter
                                    and the second element is the number.
        
        Raises:
            void
        """
        return (self.lettercoord, self.numbercoord)
