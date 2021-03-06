# Warboats_game
  Warboats is a computer game inspired by the classic Battleship game. Two players are pitted together in intense naval combat where only one can win. Using tactical thinking and a bit of luck, will you win against the computer?

### Details:
  Warboats is coded in Python and makes use of the Pygame library. The application architecture is similar to the MVC design pattern.

Authors: Genrikh Askaryan, Arnaud Michel, James Hau, Kai Li, and Weihao Liao.

### How to install:
  To install the game, simply clone the Warboats repository to the desired location on your system. No compilation of source code is required on behalf of the user since Warboats is written in Python. Note that the Pygame library is a dependency of the Warboats application so it will need to be installed on the user's system for Warboats to function properly.

### Controls of the Game:
  Use the mouse cursor and click on spaces in your grid to place your ships. Click on spaces of the computers board to guess where the computer's ships are. Clicking on the close button for the window exits the game.

### How to play:
  Warboats is a game played between the user and the computer. To start the game, navigate to the Warboats /src directory on your system and run the command ```python View.py``` from within a terminal. The game takes place on two 10 by 10 grid boards. The grids at the left and right of the application window are the player's and computer's boards respectively. The game begins in a 'placing' phase where both players will decide the locations of their ships. During the 'placing' phase, click on the positions of your board where you wish to place your ships. When you are done placing your ships, press ```enter``` on your keyboard to finalize their positions, the computer will do the same with its ships and board. After both players have placed their ships, the 'placing' phase is over and the battle begins.
  
  The game is turn-based and the player is allowed to have the first move. To guess a position on the computer's board, click on the part of the grid that you think a computer's ship may be, the guessed position is then recoloured green for 'hit' or red for 'miss'. After the player guesses, the computer will guess against the player and the result is coloured. Players will continue to take turns guessing against each other until one has sunk all of their opponent's ships. The side that succeeds in sinking all of their opponent's ships wins the game. Once the game has ended, a message is displayed in the Python terminal stating the winner.

### Screenshots

![Alt text](/screenshots/3.jpg?raw=true)
![Alt text](/screenshots/1.jpg?raw=true)
![Alt text](/screenshots/2.jpg?raw=true)

### License
  GNU general public licence version 3, 29 June 2007
� Copyright 2019, Warboats Team
### Music Credit:
http://freemusicarchive.org/music/Lobo_Loco/HEADCRASH/Experimental_Gameplay_ID_953
