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
        self.good_moves = [(-1, -1)] * depth
        self.window_size = 50

    def get_move(self, board: Board) -> Tuple[int, int]:
        overall_best_move: Tuple[int, int] = (-1, -1)
        is_maximising = self.player == 1
        previous_score = 0

        for current_search_depth in range(1, self.depth + 1):
            print(f"Searching at depth: {current_search_depth}")
            if current_search_depth == 1:
                alpha = float("-inf")
                beta = float("inf")
            else:
                alpha = previous_score - self.window_size
                beta = previous_score + self.window_size

            while True:
                best_score = float("-inf") if is_maximising else float("inf")

                start_alpha = alpha
                start_beta = beta

                moves: List[Tuple[int, int]] = board.get_active_legal_moves()
                if not moves:
                    raise RuntimeError("Called 'get_move' with no available moves")
                moves.sort(key=lambda m: board.score_move_guess(m, self.player) + self.rng.uniform(0, 0.1), reverse=True)
                current_depth_best_move = moves[0]

                if board.current_hash in self.transposition_table:
                    _, _, _, stored_move = self.transposition_table[board.current_hash]
                    if stored_move in moves:
                        moves.insert(0, moves.pop(moves.index(stored_move)))

                for move in moves:
                    x, y, z = board.apply_move(move, self.player)
                    if board.check_winner((x, y, z), self.player):
                        board.undo_move((x, y, z))
                        return move
                    
                    score = self.minimax(board, current_search_depth - 1, not is_maximising, alpha, beta)
                    board.undo_move((x, y, z))

                    if is_maximising and score > best_score:
                        best_score = score
                        current_depth_best_move = move
                        alpha = max(alpha, best_score)
                    elif not is_maximising and score < best_score:
                        best_score = score
                        current_depth_best_move = move
                        beta = min(beta, best_score)

                if best_score <= start_alpha:
                    alpha = float("-inf")
                    continue
                elif best_score >= start_beta:
                    beta = float("inf")
                else:
                    overall_best_move = current_depth_best_move
                    break

                flag = self.get_zobrist_flag(best_score, float("-inf"), float("inf"))
                self.transposition_table[board.current_hash] = (best_score, current_search_depth, flag, overall_best_move)
        return overall_best_move

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
                    self.good_moves[depth] = stored_move
                    return cached_score

        moves = board.get_active_legal_moves()
        if stored_move in moves:
            i = moves.index(stored_move)
            moves[0], moves[i] = moves[i], moves[0]
        if self.good_moves[depth] in moves:
            i = moves.index(self.good_moves[depth])
            moves[1], moves[i] = moves[i], moves[1]
            
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
                self.good_moves[depth] = move
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