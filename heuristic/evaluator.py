import numpy as np
from core.constants import directions
from core.board import Board

def evaluate_board(self, player: int, board: Board):
    score = 0
    for x, y, z in np.ndindex(board.board.shape):
        if board.board[x, y, z] == 0:
            continue

        for i in range(13):
            count = 1
            open_ends = 0

            # Check direction
            dx, dy, dz = directions[i]
            nx, ny, nz = x + dx, y + dy, z + dz
            while True:
                if not (0 <= nx < self.size and 0 <= ny < self.size and 0 <= nz < self.size):
                    break
                    
                slot = self.board[nx, ny, nz]
                
                if slot == player:
                    count += 1
                elif slot == 0:
                    open_ends += 1
                    break
                else:
                    break
                    
                nx, ny, nz = nx + dx, ny + dy, nz + dz

            # Check opposite direction
            dx, dy, dz = -dx, -dy, -dz
            nx, ny, nz = x + dx, y + dy, z + dz
            while True:
                if not (0 <= nx < self.size and 0 <= ny < self.size and 0 <= nz < self.size):
                    break
                    
                slot = self.board[nx, ny, nz]
                
                if slot == player:
                    count += 1
                elif slot == 0:
                    open_ends += 1
                    break
                else:
                    break
                    
                nx, ny, nz = nx + dx, ny + dy, nz + dz
            
            # Check evals
            score += self.score_sequence(count, open_ends)

def score_sequence(self, length: int, open_ends: int) -> int:
    if length >= 5:
        return 1_000_000
    
    if length == 4:
        if open_ends == 2:
            return 100_000
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
            return 1
    
    return 0