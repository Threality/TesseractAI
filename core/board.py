import numpy as np
from typing import Tuple, List
from core.constants import directions

"""
- Consider using a bitboard to represent the game board
- Consider using Numba for more performance
- Pytest apparently lets me easily create testing data
"""

class Board:
    def __init__(self, size: int = 9):
        self.size: int = size
        self.board = np.zeros((size, size, size))
    

    def apply_move(self, move: Tuple[int, int], player: int) -> Tuple[int, int, int]:
        x, z = move

        for i in range(self.size):
            if self.board[x, i, z] == 0:
                self.board[x, i, z] = player
                return (x, i, z)
            
        raise RuntimeError("Played a move in an invalid place!")    

    def undo_move(self, move: Tuple[int, int, int]):  
        self.board[move] = 0

    def reset(self) -> None:
        self.board = np.zeros((self.size, self.size, self.size))

    def check_winner(self, move: Tuple[int, int, int], player: int) -> bool:
        for i in range(13):
            dx, dy, dz = directions[i]
            nx, ny, nz = move[0] + dx, move[1] + dy, move[2] + dz

            # Check direction (Count = -1 so the double +1 doesnt affect outcome)
            count = 1
            while True:
                if not (0 <= nx < self.size and 0 <= ny < self.size and 0 <= nz < self.size):
                    break
                    
                slot = self.board[nx, ny, nz]
                
                if slot == player:
                    count += 1
                else:
                    break
                    
                nx, ny, nz = nx + dx, ny + dy, nz + dz

            # Check opposite direction
            dx, dy, dz = -dx, -dy, -dz
            nx, ny, nz = move[0] + dx, move[1] + dy, move[2] + dz
            while True:
                if not (0 <= nx < self.size and 0 <= ny < self.size and 0 <= nz < self.size):
                    break
                    
                slot = self.board[nx, ny, nz]
                
                if slot == player:
                    count += 1
                else:
                    break
                    
                nx, ny, nz = nx + dx, ny + dy, nz + dz
            
            # Check for winner
            if count >= 5:
                return True
        return False
    
    # AI TOOLS

    def get_state(self, player: int):
        return self.board * player
    
    def get_legal_moves(self) -> List[Tuple[int, int]]:
        out: List[Tuple[int, int]] = []

        for x in range(self.size):
            for y in range(self.size):
                if not self.is_column_full((x, y)):
                    out.append((x, y))

        return out

    # UTILITIES

    def is_column_full(self, coords: Tuple[int, int]) -> bool:
        return self.board[coords[0], self.size - 1, coords[1]] != 0