from typing import Tuple

from agents.base_agent import Agent
from core.board import Board

class PlayerAgent(Agent):
    def __init__(self, player: int, name: str):
        self.player = player
        self.name = name

    def get_move(self, board: Board) -> Tuple[int, int]:
        while True:
            try:
                x, z = input(f"{self.name} it's your move: ").split()
                x = int(x)
                z = int(z)
            except:
                print("Input must be a number")
                continue
            if min(x, z) < 0 or max(x, z) >= board.size:
                print(f"Input must be between 0 and {board.size - 1} (inclusive)")
                continue
            return x, z