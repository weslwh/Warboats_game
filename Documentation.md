## Directory Structure

- The license, README, and documentation files are located in the root folder of the Warboats repository.
- All source code for the Warboats game is located in the /src directory.
- Screenshots of the game are located in the /screenshots directory.

## Classes and Functions

Note: all classes and functions have docstrings explaining their behaviour, so we will not describe them too deeply here. Please refer to the respective class' .py file for full explanations of the code.

#### Classes

- **Board** - Represents the playing field of the Warboats game.
- **Coordinate** - Represents a postion in the Warboats game.
- **GameEngine** - Manages game logic and rules.
- **main** - the file that runs the application.
- **Player** - Represents the player entities in the Warboats game.
- **Ship** - Represents the units in the Warboats game.
- **ShipFactory** - builds ships for the Warboats game.
- **View** - the gui presented to the user.

## Extending the Game

  The Warboats game is open source and licenced under the GNU general public license, so other developers are welcome to use the source code and extend the game if they wish.

  One way to extend the game would be to add a turn timer. The turn timer would give the user a limited amount of time to choose which position to guess next. To implement the timer feature, a developer could make use of the python ```time``` class and ```time()``` function. In the game loop, when waiting for the users turn, another loop could be nexted such that while the user still has time, the game will collect the user's input, and if the user runs out of time, the game continues to let the computer guess without letting the player guess. The ```time()``` function could be used to gather the time that the player's turn starts and a later call can be used to calculate the time that has passed by taking the difference between the returned values.

  Another way to extend the game would be to add special abilites for the player to choose from. These abilities could be related to the types of ships in the warbaots game (i.e. torpedo attack, radar scan etc), but as expressed in the code the abilities might just be patterns of coordinates that would be guessed in one turn. To implement this feature, buttons could be added to the view such that when they are pressed, the subsequent guess that the player makes will be a special pattern of coordinates.
