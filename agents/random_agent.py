import random
from typing import Tuple
from agents.base_agent import Agent
from core.board import Board

class RandomAgent(Agent):
    def __init__(self):
        pass

    def get_move(self, board: Board, player: int) -> Tuple[int, int]:
        moves = board.get_legal_moves()
        return random.choice(moves)