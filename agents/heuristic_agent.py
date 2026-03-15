from typing import Tuple, List
import random
from agents.base_agent import Agent
from core.board import Board

class HeuristicAgent(Agent):
    def __init__(self, player: int, depth: int = 3, rng=random.Random()):
        self.depth = depth
        self.player = player
        self.rng = rng
        self.transposition_table = {}

    def get_move(self, board: Board) -> Tuple[int, int]:
        best_score = float("inf")
        if self.player == 1:
            best_score = float("-inf")
        best_move: Tuple[int, int] = (-1, -1)
        is_maximising = self.player == 1
        alpha = float("-inf")
        beta = float("inf")

        moves: List[Tuple[int, int]] = board.get_active_legal_moves()
        if not moves:
            raise RuntimeError("Called 'get_move' with no available moves")
        moves.sort(key=lambda m: board.score_move_guess(m, self.player) + self.rng.uniform(0, 0.1), reverse=True)

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
                beta = min(beta, best_score)

        return best_move

    def minimax(self, board: Board, depth: int, is_maximising: bool, alpha: float, beta: float) -> float:
        best_score = float("inf")
        if is_maximising:
            best_score = float("-inf")
        cur_player = 1 if is_maximising else -1
        original_alpha = alpha
        original_beta = beta
        best_move = ()
        stored_move: Tuple[int, int] = (-1, -1)

        if len(self.transposition_table) > 1_000_000:
            self.transposition_table.clear()

        if depth <= 0:
            return board.current_score
        
        if board.current_hash in self.transposition_table:
            cached_score, f_depth, flag, stored_move = self.transposition_table[board.current_hash]
            if f_depth >= depth:
                if flag == 0: # Exact
                    return cached_score
                if flag == -1: # Lowerbound
                    alpha = max(alpha, cached_score)
                elif flag == 1: # Upperbound
                    beta = min(beta, cached_score)
                if beta <= alpha:
                    return cached_score

        moves = board.get_active_legal_moves()
        moves.sort(key=lambda m: board.score_move_guess(m, cur_player), reverse=True)
        if stored_move in moves:
            i = moves.index(stored_move)
            moves[0], moves[i] = moves[i], moves[0]
            
        for move in moves:
            x, y, z = board.apply_move(move, cur_player)
            if board.check_winner((x, y, z), cur_player):
                if is_maximising:
                    best_score = 100_000_000 + depth
                    alpha = max(best_score, alpha)
                elif not is_maximising:
                    best_score = -100_000_000 - depth
                    beta = min(best_score, beta)
                board.undo_move((x, y, z))
                return best_score
            score = self.minimax(board, depth - 1, not is_maximising, alpha, beta)
            if is_maximising and score > best_score:
                best_score = score
                alpha = max(best_score, alpha)
                best_move = move
            elif not is_maximising and score < best_score:
                best_score = score
                beta = min(best_score, beta)
                best_move = move
            board.undo_move((x, y, z))
            if beta <= alpha:
                break
            
        if  not best_move:
            best_move = moves[0]
        flag = self.get_zobrist_flag(best_score, original_alpha, original_beta)
        self.transposition_table[board.current_hash] = (best_score, depth, flag, best_move)
        
        return best_score
    
    def get_zobrist_flag(self, best_score: float, alpha: float, beta: float) -> int:
        if best_score <= alpha:
            return 1
        if best_score >= beta:
            return -1
        else:
            return 0