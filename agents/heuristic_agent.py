from typing import Tuple, List
from agents.base_agent import Agent
from core.board import Board
from heuristic.evaluator import full_board_evaluation

class HeuristicAgent(Agent):
    def __init__(self, player: int, depth: int = 3):
        self.depth = depth
        self.player = player

    def get_move(self, board: Board) -> Tuple[int, int]:
        best_score = float("inf")
        if self.player == 1:
            best_score = float("-inf")
        best_move: Tuple[int, int] = (-1, -1)
        is_maximising = self.player == 1
        alpha = float("inf")
        beta = float("-inf")

        moves: List[Tuple[int, int]] = board.get_legal_moves()
        if not moves:
            raise RuntimeError("Called 'get_move' with no available moves")

        for move in moves:
            x, y, z = board.apply_move(move, self.player)
            if board.check_winner((x, y, z), self.player):
                board.undo_move((x, y, z))
                return move
            score = self.minimax(board, self.depth - 1, not is_maximising, alpha, beta)
            board.undo_move((x, y, z))
            if is_maximising and score > best_score:
                best_score = score
                best_move = move
                alpha = max(alpha, best_score)
            elif not is_maximising and score < best_score:
                best_score = score
                best_move = move
                alpha = max(alpha, best_score)

        return best_move

    def minimax(self, board: Board, depth: int, is_maximising: bool, alpha: float, beta: float) -> float:
        best_score = float("inf")
        if is_maximising:
            best_score = float("-inf")
        cur_player = 1 if is_maximising else -1

        if depth <= 0:
            return full_board_evaluation(board)

        moves = board.get_legal_moves()
        for move in moves:
            x, y, z = board.apply_move(move, cur_player)
            if board.check_winner((x, y, z), cur_player):
                if is_maximising:
                    best_score = 1_000_000
                    alpha = max(best_score, alpha)
                elif not is_maximising:
                    best_score = -1_000_000
                    beta = min(best_score, beta)
                board.undo_move((x, y, z))
                return best_score
            score = self.minimax(board, depth - 1, not is_maximising, alpha, beta)
            if is_maximising and score > best_score:
                best_score = score
            elif not is_maximising and score < best_score:
                best_score = score
            board.undo_move((x, y, z))
            if beta <= alpha:
                break

        return best_score