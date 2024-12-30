from dataclasses import dataclass
from enum import Enum


class GameStates(Enum):
    IN_PLAY = "in_play"
    WON = "won"
    DRAW = "draw"

class GameMoves:
    UP = -1
    RIGHT = 1
    DOWN = 1
    LEFT = -1


class GamePiece(Enum):
    CROSS = "x"
    CIRCLE = "O"
    EMPTY = " "

@dataclass
class Player:
    name:str
    piece:GamePiece
    index:int