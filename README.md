# IS211_Assignment7


# Pig Game

Welcome to the Pig game, a classic dice game where players roll a die and accumulate points in a quest to reach 100 points first. This simple yet strategic game involves deciding whether to risk rolling again for more points or to hold and secure your current turn total. This implementation allows for a customizable number of players and introduces "Magic Tokens" for an added twist, enhancing the traditional game with new strategies and fun.

# Features

- Play with 2 to N players, where N can be defined at the start of the game.
- "Magic Tokens" feature that introduces strategic elements and surprises.
- Command-line interface for easy and accessible gameplay.
- Consistent game experience with a seedable random number generator.

# Getting Started

To start playing the Pig game, ensure you have Python installed on your computer. This game has been tested with Python 3.8 and above.

# Installation

No additional installation is required. Simply clone this repository or download the source code to your local machine.

# Running the Game

Navigate to the project directory where the game files are located and run the following command in your terminal or command prompt:

sh
python pig.py --numPlayers=<number_of_players>


Replace `<number_of_players>` with the desired number of players. If no number is specified, the game defaults to 2 players.

Example:

sh
python pig.py --numPlayers=4


# How to Play

The game follows the traditional rules of Pig with the addition of Magic Tokens. On each turn, a player rolls a die and accumulates points. The player can choose to "hold," adding their turn total to their overall score, or risk rolling again. Rolling a 1 ends the player's turn and forfeits their turn total. The first player to reach or exceed 100 points wins.

 # Magic Tokens

Players can earn Magic Tokens during the game based on specific achievements, such as rolling doubles or reaching a high turn total. Tokens can be used to:

- Skip: Skip the next player's turn.
- Steal: Steal points from another player.
- Shield: Protect against losing points if a 1 is rolled.
- Double-Up: Double the points on the next roll.

Use tokens strategically to gain an advantage over your opponents!

