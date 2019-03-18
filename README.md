# Warboats_game


Warboats is a game based off of the classic battleship game. Two players are pitted together in intense naval combat, 
where only one can win.

**Details**:

  Warboats is coded using pythons pygame library, using a MVC design pattern. Project completed for CSC290 at the University of Toronto Mississauga, 2019. Team members: Genrikh Askaryan, Arnaud Michel, James Hau, Kai Li, and Weihao Liao.
  
  Feel free to download and use our work however you please.

**How to install**:
  To install the game, simply clone the Warboats repository. Since the game is written in Python, no compilation is requred on behalf of the user, just run 'main.py' and a window will appear for the game. Note that Warboats makes use of the Pygame library, so it will need to be installed in order to play the game.

**How to play**:
  Warboats is a game consisting of two players: You and the computer. The game takes place on two 10 by 10 grid boards, where each player guesses positions on their opponents board. At the start of the game you must place a set of ships onto the board, where the location of the ships will be hidden from the computer. The computer will do the same, and your goal is to find where all the computers ships are hidden by guessing the correct coordinates.
  
  The game is turn-based and the player is allowed to have the first guess, then the game will let the computer guess on the player's board. After that, the player gets to guess again. This repeats until either the player or computer have sunk all of their opponent's ships. The side that succeeds in sinking all of their opponent's ships wins the game. 

  The game is to be played using the mouse cursur after starting the application (main.py). The grid board at the top of the window is the computer's board, the one closer to the bottom is the player's board. The player guesses on the computer's board by clicking on one of the boxes on the computer's board. Warboats signifies 'hits' and 'misses' as red and blue boxes respectively. When the game is over, a message is displayed that states the winner of the game.

**Screenshots**


**License**
  GNU general public licence version 3, 29 June 2007
