import Ship


class ShipFactory:
    """
    The ShipFactory class builds Ship objects
    
    Methods:
        build(ship_type, coordinates)
    """
    def build(ship_type, coordinates):
        """
        Builds and returns a Ship object with the specified type and 
        coordinates.
        
        Args:
            type (String): The type of the ship to be built.
            coordinates (List[Coordinate]): The coordinates of the ship to be built.
            
        Returns:
            build_ship (Ship): The ship that was built.
        
        Raises:
            void
        """
        s = Ship()
        s.set_ship_coordinates(coordinates)
        s.set_type(ship_type)
        return s


