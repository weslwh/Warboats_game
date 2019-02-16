class board:
    """
    Represent the cooordinates function to the UI for display
    """
    def __init__(self, x:str, y:int, game_engine:object):
        """
        Initial the attributes x 
        """
        self.x = x
        self.y = y
        self.hit_coordinates = []
        self.miss_coordinates = []
        self.game_engine = game_engine
        
    def is_valid_cooridinate(self, c: coordinate):
        """
        Return True if the cooridinate is valid, otherwise return False
        """
        if (c.get_letter() in self.x) and (c.get_number() in self.y):
                return True
        return False
        
    def add_hits(self, c: coordinate):
        """
        Append the hits position into hit_coordinates list
        """
        if guess_position():
            self.hit_coordinate.append(c.get_ship_coordinate)

    def get_hits():
        """
        Return the list of hit
        """
        return self.hit_coordinate()
            
    def add_miss(c: coordinate):
        """
        Append the miss position into miss_coordinates list
        """
        if not guess_position():
            self.miss_coordinates.append(c)

    def get_misses(c:coordinate):
        """
        Return the list of miss
        """
        return self.hit_coordinate()

    def guess_coordinate(c:coordinate):
        """
        input player guess coordinate to the game engine
        """
        game_engine.guess_position(c)
        
        


