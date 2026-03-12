from core.board import Board
from core.game import Game
from agents.random_agent import RandomAgent
from agents.heuristic_agent import HeuristicAgent

def run_single_vs_game():
    board = Board(size=9)
    agent1 = HeuristicAgent(1, depth=2)
    agent2 = HeuristicAgent(-1, depth=2)

    game = Game(board, agent1, agent2)
    winner = game.play(verbose=True)
    print(f"Game Over. Result: {winner}")

if __name__ == "__main__":
    run_single_vs_game()