from typing import Tuple, List
from agents.base_agent import Agent
from core.board import Board

class HeuristicAgent(Agent):
    def __init__(self, player: int, depth: int = 3):
        self.depth = depth
        self.player = player

    def get_move(self, board: Board) -> Tuple[int, int]:
        best_score = float("inf")
        if self.player == 1:
            best_score = float("-inf")
        best_move = None
        is_maximising = self.player == 1

        moves: List[Tuple[int, int]] = board.get_legal_moves()
        for move in moves:
            x, y, z = board.apply_move(move, self.player)
            score = self.minimax(board, self.depth, is_maximising)
            board.undo_move((x, y, z))
            if is_maximising and score > best_score:
                best_score = score
                best_move = move
            elif not is_maximising and score < best_score:
                best_score = score
                best_move = move
            
    def minimax(self, board: Board, depth: int, is_maximising: bool) -> float:
        moves = board.get_legal_moves()
        for move in moves:
            x, y, z = board.apply_move(move, self.player)
            score = self.minimax(board, self.depth, self.player==1)
            board.undo_move((x, y, z))