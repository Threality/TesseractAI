from abc import abstractmethod
from typing import Tuple
from core.board import Board

class Agent:
    @abstractmethod
    def get_move(self, board: Board, player: int) -> Tuple[int, int]:
        raise RuntimeError("'get_move' was not overwritten!")