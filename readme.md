# Tic-Tac-Toe Game

## Introduction
This is a basic implementation of the tic-tac-toe game which runs within the terminal. The game allows two players to compete against each other by taking turns to place their game pieces on a 3x3 grid. The objective is to get three of your game pieces in a row, either horizontally, vertically, or diagonally.

## Installation Instructions
1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine using:
    ```sh
    git clone https://github.com/alquindev/py-tic-tac-toe.git  
    ```
3. Navigate to the project directory:
    ```sh
    cd TicTakToeGame/Game
    ```

## Getting Started
1. To start the game, run the [run.bat](http://_vscodecontentref_/1) file or execute the following command in your terminal:
    ```sh
    py main.py
    ```
2. Follow the on-screen instructions to play the game.

## User Manual
### Controls
- **Left Arrow**: Move cursor left
- **Right Arrow**: Move cursor right
- **Up Arrow**: Move cursor up
- **Down Arrow**: Move cursor down
- **Space Bar**: Place your game piece on the board
- **'r' Key**: Restart the game
- **'h' Key**: View the instructions
- **'esc' Key**: Exit the game

### Objective
- The goal is to get three of your game pieces in a row, either horizontally, vertically, or diagonally.

### Players
- **Player 1**: CROSS (X)
- **Player 2**: CIRCLE (O)

## API Documentation
### Classes
- [Board](https://github.com/alquindev/py-tic-tac-toe/blob/main/Board.py): Manages the game board and its state.
- [GamePlay](https://github.com/alquindev/py-tic-tac-toe/blob/main/GamePlay.py): Handles the game logic and player interactions.
- [Player](https://github.com/alquindev/py-tic-tac-toe/blob/main/Player.py): Represents a player in the game.
- [Components](https://github.com/alquindev/py-tic-tac-toe/blob/main/Components.py): Contains enums and data classes used in the game.

### Methods
- [Board.draw()](https://github.com/alquindev/py-tic-tac-toe/blob/main/Board.py#L160): Draws the current state of the board.
- [GamePlay.start()](https://github.com/alquindev/py-tic-tac-toe/blob/main/GamePlay.py#L48): Starts the game and listens for player inputs.
- [GamePlay.restart()](https://github.com/alquindev/py-tic-tac-toe/blob/main/GamePlay.py#L65): Restarts the game.
- [GamePlay.redraw()](https://github.com/alquindev/py-tic-tac-toe/blob/main/GamePlay.py#L73): Redraws the game board.
- [GamePlay.update_game_state()](https://github.com/alquindev/py-tic-tac-toe/blob/main/GamePlay.py#L79): Updates the game state based on the current board.

## Troubleshooting
### Common Issues
- **Game not starting**: Ensure you have Python installed and you are running the correct file.
- **Controls not working**: Make sure your terminal window is focused and you are pressing the correct keys.

## FAQ
### How do I change the size of the board?
- The board size is currently fixed at 3x3. You can modify the [Board](https://github.com/alquindev/py-tic-tac-toe/blob/main/Board.py) class in [Board.py](https://github.com/alquindev/py-tic-tac-toe/blob/main/Board.py#L92) to change the dimensions.

### Can I play against a computer?
- This implementation only supports two human players. You can extend the game logic to add AI functionality.

## Appendices
### References
- [Python Official Documentation](https://docs.python.org/3/)
- GitHub Repository

### Resources
- [Tic-Tac-Toe Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)