#author: am222666

PLACING_PHASE = 'placing'
PLAYING_PHASE = 'playing'

class Game_Engine:
    '''
    Game_Engine class to represent game logic of the Warboats game.
    
    Methods:
        __init__(self, player, computer, board, ship_factory)
        game_won(self)
        players_still_playing(self)
        update_game_won(self)
        guess_position(self, coord, p)
        init_player(self, p, coords)
    '''
    
    def __init__(self, player, computer, board, ship_factory):
        '''
        Initialize a game engine object with two Player objects 
        and a Board object.
        
        Args:
            player (Player): to represent the user of the application.
            computer (Player): to represent the computer the user plays 
				against.
            board (Board): to represent the grid warboats takes place on.
            ship_factory (Ship_Factory): used for building ships to add to
                                        players.
            
        Returns:
            void.
            
        Raises:
            void.
        '''
        
        self.players = [player, computer]
        self.game_won = False
        self.game_state = PLACING_PHASE
        self.board = board
        self.factory = ship_factory

       
    def game_won(self):
        '''
        Return True if the game is in a winning state.
        
        Args:
            void.
        
        Returns:
            won (Boolean): True if the game is in a winning state.
                            
        Raises:
            void.
        '''
        return self.game_won

    
    def players_still_playing(self):
        '''
        Returns a list of Player objects from the game engine that 
        still have ships, and thus are still able to participate in the
        game. Note: if the list is of length 1, then that is the Player
        object that has won the game.
        
        Args:
            void.
        
        Returns:
            players (List[Player]): a list of all the players who still
					have unsunk ships.
        
        Raises:
            void.
        '''
        players_still_playing = []
        for player in self.players:
            if player.still_has_ships():
                players_still_playing.append(player)
            
        return players_still_playing

    
    def update_game_won(self):
        if len(self.players_still_playing()) == 1:
            self.game_won = True


    def guess_position(self, coord, p):
        '''
        Guess Coordinate coord against Player p. If coordinate is a 'hit',
        adds that coordinate to the 'hits' of the board. Likewise, 
        if it is a 'miss', adds the coordinate to the 'misses' of the 
		board.
        
        Returns True if a guess is successfully made against Player p,
        False otherwise.
        
        Args:
            coord (Coordinate): the coordinate of interest.
            p (Player): the player to be guess coord against.
            
        Returns:
            success (Boolean): if a guess was successfully made.
            
        Raises:
            void.
        '''
        if not p in self.players:
            return False #Player object provided was not part of this game
        
        if p.guess_position(coord):
            self.board.add_hit(coord)
        else:
            self.board.add_miss(coord) 
        return True

    
    def init_player(self, p, coords):
        '''
        Adds ships to Player p with the coordinates specified in the List
        coords. 
        Returns True on successful completion and False if p is
        not one of the players contained in this Game_Engine.
        
        Args:
            p (Player): the player to add ships to.
            coords (List[coordinate]): a list of coordinates to initialize 
                                        ships with.
                                        
        Returns:
            success (Boolean): if the entire list is processed successfully
                                into unique ships for the player.
                                
        Raises:
            void.
        '''
        player_to_add_to = None
        for player in self.players:
            if player == p:
                player_to_add_to = player
                
        if player_to_add_to == None:
            return False #Player p was not in the list of players
        
        for ship_coord_list in coords:
            ship = self.factory.build('boat', ship_coord_list)
            
            if not player_to_add_to.add_ships(ship):
                return False #problem adding ships to player
            
        return True
