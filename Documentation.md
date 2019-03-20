## Directory Structure

  The license, README, and documentation are located in the root folder of the repository.
  All source code for the Warboats game is located in the /src directory.

## Classes and Functions

Note: all classes and functions have docstrings explaining their behaviour, so we will not describe them too deeply here. Please refer to the respective class' .py file for full explanations of the code.

#### Classes

**Board** - Represents the playing field of the Warboats game.
**Coordinate** - Represents a postion in the Warboats game.
**GameEngine** - Manages game logic and rules.
**main** - the file that runs the application.
**Player** - Represents the player entities in the Warboats game.
**Ship** - Represents the units in the Warboats game.
**ShipFactory** - builds ships for the Warboats game.
**View** - the gui presented to the user.

## Extending the Game

  To extend the game, a developer can use the Warboats code as a base for adding more features to the game. One example would be implementing a turn timer, so that the player has a limited amount of time to choose which position to guess. To do this, a timer could be added in the main.py file inside the loop that runs the game. The timer could be implemented so that the player's turn ends and the computer guesses again.

  Another way to extend the game would be to add special abilites for the player to choose from. These abilities could be related to the types of ships in the warbaots game (i.e. torpedo attack, radar scan etc), but as expressed in the code the abilities might just be patterns of coordinates that would be guessed in one turn. To implement this feature, buttons could be added to the view such that when they are pressed, the subsequent guess that the player makes will be a special pattern of coordinates.
