from agents.base_agent import Agent
from core.board import Board
import random

class RandomAgent(Agent):
    def __init__(self):
        pass
    
    def get_move(self, board: Board):
        moves = board.get_legal_moves()
        return random.choice(moves)