import numpy as np
from typing import Tuple

class Board:
    def __init__(self, size: int = 9):
        self.size = size
        self.board = np.zeros((size, size, size))
        self.directions = {
                            0:  [1, 0, 0],
                            1:  [0, 1, 0],
                            2:  [0, 0, 1],

                            3:  [1, 1, 0],
                            4:  [1, -1, 0],
                            5:  [1, 0, 1],
                            6:  [1, 0, -1],
                            7:  [0, 1, 1],
                            8:  [0, 1, -1],

                            9:  [1, 1, 1],
                            10: [1, 1, -1],
                            11: [1, -1, 1],
                            12: [1, -1, -1],
                        }
    
    def apply_move(self, move: Tuple[int, int], player: int) -> None:
        x, z = move
        for i in range(self.size):
            if self.board[x, i, z] == 0:
                self.board[x, i, z] = player
                return
        raise RuntimeError("Played a move in an invalid place!")      

    def reset(self) -> None:
        self.board = np.zeros((self.size, self.size, self.size))

    def check_winner(self, move: Tuple[int, int, int], player: int) -> bool:
        for i in range(13):
            new_pos = move
            dx, dy, dz = self.directions[i]
            count = 0
            while self.board[new_pos] == player:
                count += 1
                new_pos = move[0] + dx, move[1] + dy, move[2] + dz
                if min(new_pos) < 0 or max(new_pos) >= self.size:
                    break
            if count >= 5:
                return True
        return False
    
    def get_state(self, player: int):
        return self.board * player