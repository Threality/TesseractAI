from abc import abstractmethod
from typing import Tuple
from core.board import Board

class Agent:
    @abstractmethod
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        raise RuntimeError("'get_move' was not overwritten!")