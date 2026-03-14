from core.board import Board
from core.game import Game
from agents.random_agent import RandomAgent
from agents.heuristic_agent import HeuristicAgent, LocalHeuristicAgent

def run_single_vs_game():
    board = Board(size=9)
    agent1 = LocalHeuristicAgent(1, depth=3)
    agent2 = HeuristicAgent(-1, depth=3)

    game = Game(board, agent1, agent2)
    winner = game.play(visualise=True)
    print(f"Game Over. Result: {winner}")

if __name__ == "__main__":
    run_single_vs_game()