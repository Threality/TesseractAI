from core.board import Board
from core.constants import symbols
from agents.base_agent import Agent
from utils.visualiser import Visualiser

class Game:
    def __init__(self, board: Board, agent_1: Agent, agent_2: Agent):
        self.board = board
        self.agent1 = agent_1
        self.agent2 = agent_2
        self.cur_player = 1
    
    def play(self, verbose=False, stepped=False, visualise=False):
        self.board.reset()
        if visualise:
            visualiser = Visualiser()

        while True:
            active_agent = self.agent1 if self.cur_player == 1 else self.agent2

            move = active_agent.get_move(self.board)

            x, y, z = self.board.apply_move(move, self.cur_player)
            
            if verbose:
                self.print_board()
            if visualise:
                visualiser.plot_board(self.board) # type:ignore

            if self.board.check_winner((x, y, z), self.cur_player):
                if verbose:
                    print(f"Player {self.cur_player} wins!")
                return self.cur_player
            
            if len(self.board.get_legal_moves()) == 0:
                return 0
            
            self.cur_player *= -1

            if stepped:
                input("Step?")

    def print_board(self):
        size = self.board.size
        for y in range(size):
            print(f"\nLayer {y}")
            print("-" * (size * 2))

            for z in reversed(range(size)):
                row = ""
                for x in range(size):
                    row += symbols[self.board.board[x, y, z]] + " "
                print(row)

            print("-" * (size * 2))