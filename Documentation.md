## Directory Structure

- The license, README, and documentation files are located in the root folder of the Warboats repository.
- All source code for the Warboats game is located in the /src directory.
- Screenshots of the game are located in the /screenshots directory.

## Classes and Functions

Note: all classes and functions have docstrings explaining their behaviour, so we will not describe them too deeply here. Please refer to the respective class' .py file for full explanations of the code.

#### Classes

- **Board** - Represents the playing field of the Warboats game.
  - **is_valid_coordinate(...)** - checks if a coordinate is valid in the board.
  - **add_hits(...)** - add a hit to the board.
  - **add_miss(...)** - add a miss to the board.
  - **get_hits()** - get the hits of the board.
  - **get_misses()** - get the misses of the board.
  - **guess_coordinate(...)** - guess a coordinate and update the board.
- **Coordinate** - Represents a postion in the Warboats game.
  - **get_letter()** - return the lettervalue  of a coordinate.
  - **get_number()** - return the number value of a coordinate.
  - **get_tuple()** - return a tuple representation of a coordinate.
- **GameEngine** - Manages game logic and rules.
  - **game_won()** - returns ```True``` if the game is won.
  - **players_still_playing()** - return a list of players still active in the game.
  - **update_game_won()** - updates the win status of the game.
  - **guess_position(...)** - guesses a position against a player.
  - **init_player(...)** - initializes a player and their ships.
- **Player** - Represents the player entities in the Warboats game.
  - **add_ships(...)** - add ships to a player.
  - **get_ships()** - return a list of ships that the player has.
  - **guess_position(...)** - returns ```True``` if a player has a ship at the coordinate.
  - **still_has_ships()** - return ```True``` if the player still has ships.
- **Ship** - Represents the units in the Warboats game.
  - **get_ship_coordinates()** - return the list of coordinates for this ship.
  - **guess_position(...)** - guess a position against this ship.
  - **set_ship_coordinates(...)** - set the coordinates of a ship.
  - **is_sunk()** - return ```True``` if the ship is sunk.
- **ShipFactory** - builds ships for the Warboats game.
  - **build(...)** - build a ship with coordinates and a type.

#### files

- **View.py** - The application starting point. Also presents the gui to the user.
- **Grid.py** - contains helper code for drawing the boards.
- **Square.py** - contains helper code for drawing segments of the board.
- **Game_Engine.py** - contains the logic for the game loop of the application.

## Extending the Game

  The Warboats game is open source and licenced under the GNU general public license, so other developers are welcome to use the source code and extend the game if they wish.

  One way to extend the game would be to add a turn timer. The turn timer would give the user a limited amount of time to choose which position to guess next. To implement the timer feature, a developer could make use of the python ```time``` class and ```time()``` function. In the game loop, when waiting for the users turn, another loop could be nexted such that while the user still has time, the game will collect the user's input, and if the user runs out of time, the game continues to let the computer guess without letting the player guess. The ```time()``` function could be used to gather the time that the player's turn starts and a later call can be used to calculate the time that has passed by taking the difference between the returned values.

  Another way to extend the game would be to add special abilites for the player to choose from. These abilities could be related to the types of ships in the warbaots game (i.e. torpedo attack, radar scan etc), but as expressed in the code the abilities might just be patterns of coordinates that would be guessed in one turn. To implement this feature, buttons could be added to the view such that when they are pressed, the subsequent guess that the player makes will be a special pattern of coordinates.
