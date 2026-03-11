import random
from typing import Tuple
from agents.base_agent import Agent
from core.board import Board

class RandomAgent(Agent):
    def get_move(self, board: Board) -> Tuple[int, int]:
        moves = board.get_legal_moves()
        return random.choice(moves)