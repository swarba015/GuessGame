# Guess Game - A Decision Tree Based Interactive Game
## Description
Guess Game is an interactive Python game that utilizes a decision tree to guess objects based on user responses. It's a learning game that evolves over time as it learns from the users' inputs.

## Features
### Interactive Gameplay: 
Players interact with the game by answering yes/no questions, leading the game to guess the object they are thinking of.
### Learning Ability: 
The game learns and expands its decision tree based on new information provided by users when it makes a wrong guess.
### Save and Load Functionality: 
Players can save the current state of the decision tree to a file and load it in subsequent sessions, allowing the game to retain its learning over time.
### Tree Visualization: 
The game provides a function to print the current state of the decision tree, helping in debugging and understanding its structure.

### How to Play
1. Start the Game: Run main() to start the game.
2. Load a Tree (Optional): You can choose to load a pre-existing decision tree from a file.
3. Answer Questions: The game will ask a series of yes/no questions.
4. Game Guesses: Based on your responses, the game will make a guess.
5. Correcting Wrong Guesses: If the guess is wrong, you can teach the game by providing the right answer and a distinguishing question.
6. Play Again or Exit: After each round, choose to play again or exit. You can save the current tree state before exiting.

   
## Requirements
Python 3.x
Basic understanding of Python and command-line interaction

## Installation
No additional installation is required. Just clone the repository and run the script in a Python environment.

## Usage
To play the game, execute the main() function in the script. Follow the on-screen prompts to interact with the game.

