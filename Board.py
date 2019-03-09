class Board:
    """
    The Board class is used to store
    the cooordinates relevance to the Warboats game instance.

    Methods:
        __init__(self, h_dimension:str, v_dimension:int, game_engine:object)
        is_valid_cooridinate(self, c: coordinate)
        add_hits(self, c: coordinate)
        get_hits()
        add_miss(c: coordinate)
        get_misses(c: coordinate)
        guess_coordinate(c: coordinate)
    """
    
    def __init__(self, h_dimension, v_dimension, game_engine):
        """
        Initial the attributes Coordinate to be horizontal
        dimension and vertical dimension, and pass the reference
        to the GameEngine instance.

        Args:
            h_dimension(int): The horizatal dimension
            v_dimension(int):  The vertical dimension
            game_engin(object): GameEngine

        Returns:
            void
            
        Raises:
            void
        """
        self.h_dimension = h_dimension
        self.v_dimension = v_dimension
        self.hit_coordinates = []
        self.miss_coordinates = []
        self.game_engine = game_engine
        
    def is_valid_cooridinate(self, coordinate):
        """
        Return True if the cooridinate is in the range of the board's coordinates,
        otherwise return False

        Args:
            coordinate (Coordinate): coordinate to check

        Returns:
            (boolean): is the coordinate is valid(in the range of board)
            
        Raises:
            void
        """
        if (coordinate.get_letter() in self.h_dimension) and \
           (coordinate.get_number() in self.v_dimension):
                return True
        return False
        
    def add_hits(self, coordinate):
        """
        Append the hits position into hit_coordinates list

        Args:
             coordinate (Coordinate): coordinate to check

        Returns:
            void
            
        Raises:
            voids
        """
        if guess_position():
            self.hit_coordinate.append(c.get_ship_coordinate)

    def get_hits(self):
        """
        Return the list of hit

        Args:
            void

        Returns:
            hit_coordinate(list): The list includes all hit coordinate
            
        Raises:
            void
        """
        return self.hit_coordinate()
            
    def add_miss(self, coordinate):
        """
        Append the miss position into miss_coordinates list

        Args:
            coordinate (Coordinate): coordinate to check

        Returns:
            void

        Raises:
            void
        """
        if not guess_position():
            self.miss_coordinates.append(c)

    def get_misses(self, coordinate):
        """
        Return the list of miss

        Args:
           coordinate (Coordinate): coordinate to check

        Returns:
           miss_coordinate(list): The list includes all miss coordinate
            
        Raises:
            void
        """
        return self.miss_coordinate()

    def guess_coordinate(self, coordinate):
        """
        Input player guess coordinate to the game engine

        Args:
           coordinate (Coordinate): coordinate to check

        Returns:
            void

        Raises:
            void
        """
        game_engine.guess_position(c)
        
        


