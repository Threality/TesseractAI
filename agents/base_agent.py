from abc import abstractmethod
from core.board import Board

class Agent:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_move(self, board: Board):
        raise RuntimeError("'get_move' was not overwritten!")