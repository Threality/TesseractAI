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
    score = 0
    for i in range(13):
            center = [board.board[move]]
            left = []
            right = []

            # Check direction
            dx, dy, dz = directions[i]
            nx, ny, nz = move[0] + dx, move[1] + dy, move[2] + dz
            while True:
                if not (0 <= nx < board.size and 0 <= ny < board.size and 0 <= nz < board.size):
                    break
                right.append(board.board[nx, ny, nz])
                nx, ny, nz = nx + dx, ny + dy, nz + dz

            # Check opposite direction
            dx, dy, dz = -dx, -dy, -dz
            nx, ny, nz = move[0] + dx, move[1] + dy, move[2] + dz
            while True:
                if not (0 <= nx < board.size and 0 <= ny < board.size and 0 <= nz < board.size):
                    break
                left.append(board.board[nx, ny, nz])
                nx, ny, nz = nx + dx, ny + dy, nz + dz

            line = left[::-1] + center + right
            score += evaluate_line(line)

    return score

def evaluate_line(line: List[int]) -> float:
    i = 0
    score = 0
    while i < len(line):
        length = 0
        opens = 0
        if line[i] == 0:
            i += 1
            continue
        start = i
        while i < len(line) and line[i] == 1:
            length += 1
            i += 1
        end = i

        if length != 0:
            if start > 0 and line[start - 1] == 0:
                opens = 1
            if end < len(line) and line[end] == 0:
                opens += 1
            score += score_sequence(length, opens)
            length = 0
            opens = 0

        start = i
        while i < len(line) and line[i] == -1:
            length += 1
            i += 1
        end = i

        if length != 0:
            if start > 0 and line[start - 1] == 0:
                opens = 1
            if end < len(line) and line[end] == 0:
                opens += 1
            score -= score_sequence(length, opens)

    return score