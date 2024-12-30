from Board import Board
from Components import GameMoves, GamePiece, GameStates, Player
import os
import keyboard


class GamePlay:
    _active_player:int
    _players:list[Player]
    _board:Board
    _game_state:GameStates
    _instructions = """
    Welcome to TicTacToe Game!

    Instructions:
    1. Use the arrow keys to move the cursor on the board:
        - Left Arrow: Move left
        - Right Arrow: Move right
        - Up Arrow: Move up
        - Down Arrow: Move down

    2. Press the space bar to place your game piece on the board.

    3. Press 'r' to restart the game.

    4. Press 'h' to view the instructions.

    5. Press 'esc' to exit the game.

    Objective:
    - The goal is to get three of your game pieces in a row, either horizontally, vertically, or diagonally.

    Players:
    - Player 1: CROSS
    - Player 2: CIRCLE

    Enjoy the game!
"""
    def __init__(self, player1:Player = Player("Player 1", GamePiece.CROSS, 0), player2:Player = Player("Player 2", GamePiece.CIRCLE, 1)):
        self._board = Board()
        if player1.piece == player2.piece:
            raise ValueError("Player 1 and 2 cannot have the same game piece.")
        self._players = [player1, player2]
        self._active_player=0
        self._game_state = GameStates.IN_PLAY


    def start(self):
        self._heading()
        self._board.draw()
        # Movement
        keyboard.on_press_key("left", self._move_left)
        keyboard.on_press_key("right", self._move_right)
        keyboard.on_press_key("down", self._move_down)
        keyboard.on_press_key("up", self._move_up)

        keyboard.on_press_key("r", self._restart)
        keyboard.on_press_key("h", self._help)

        keyboard.on_press_key("space", self._place_piece)
        keyboard.wait("esc")
        print("Game Over")


    def restart(self):
        self._board = Board()
        self._active_player=0
        self._game_state = GameStates.IN_PLAY
        self.redraw()



    def redraw(self):
        os.system("cls")
        self._heading()
        self._board.draw()
        

    def update_game_state(self):
        self._game_state = self._board.get_state(self._players[self._active_player].piece)
        return self._game_state
    
    def _move_left(self, event):
        if event.event_type == "down":
            self._board.horizointal_movement(GameMoves.LEFT)
            self.redraw()
    
    def _move_right(self,event):
        if event.event_type == "down":
            self._board.horizointal_movement(GameMoves.RIGHT)
            self.redraw()

    def _move_down(self, event):
        if event.event_type == "down":
            self._board.vertical_movement(GameMoves.DOWN)
            self.redraw()

    def _move_up(self, event):
        if event.event_type == "down":
            self._board.vertical_movement(GameMoves.UP)
            self.redraw()

    def _place_piece(self, event):
        if  (event.event_type != "down" or self._game_state != GameStates.IN_PLAY): 
            return
        piece = self._players[self._active_player].piece
        if self._board.place_piece(piece):
            self.update_game_state()
            if self._game_state == GameStates.IN_PLAY:
                self._next_player()
            self.redraw()

    def _restart(self, event):
        if event.event_type == "down":
            self.restart()

    def _help(self, event):
        if event.event_type == "down":
            print(self._instructions)


    def _next_player(self):
        self._active_player = (self._active_player + 1)  % len(self._players)
        return self._active_player

    def _heading(self):
        print("Active Player: ", self._players[self._active_player].name)
        print("State: ", self._game_state.value.upper())

