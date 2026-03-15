import numpy as np
from typing import Tuple, List
from core.constants import directions

def score_sequence(length: int, open_ends: int) -> int:
    if length >= 5:
        return 100_000_000
    
    if length == 4:
        if open_ends == 2:
            return 1_000_000
        elif open_ends == 1:
            return 10_000
    
    if length == 3:
        if open_ends == 2:
            return 1000
        elif open_ends == 1:
            return 100
    
    if length == 2:
        if open_ends == 2:
            return 10
        elif open_ends == 1:
            return 5
        
    if length == 1:
        return 1
    
    return 0

def calculate_positions_score(move: Tuple[int, int, int], board) -> float:
    total_score = 0

    for i in range(13):
            # Set position to edge of that direction
            dx, dy, dz = directions[i]

            # Go to the edge of the board
            nx, ny, nz = move
            while 0 <= nx < board.size and 0 <= ny < board.size and 0 <= nz < board.size:
                nx, ny, nz = nx - dx, ny - dy, nz - dz
            nx += dx
            ny += dy
            nz += dz

            length = 0
            open_before = 0
            current_player = board.board[nx, ny, nz]

            # Scan along the whole axis
            while 0 <= nx < board.size and 0 <= ny < board.size and 0 <= nz < board.size:
                slot = board.board[nx, ny, nz]

                if slot == current_player and slot != 0:
                    length += 1
                else:
                    if length > 0:
                        open_after = 1 if slot == 0 else 0
                        score = score_sequence(length, open_before + open_after)
                        total_score += score if current_player == 1 else -score
                    
                    if slot == 0:
                        open_before = 1
                        current_player = 0
                        length = 0
                    else:
                        open_before = 1 if current_player == 0 else 0
                        current_player = slot
                        length = 1
                nx += dx
                ny += dy
                nz += dz
            
            if length > 0:
                score = score_sequence(length, open_before)
                total_score += score if current_player == 1 else -score

    return total_score