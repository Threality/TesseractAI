import random
from core.board import Board
from core.game import Game
from agents.player_agent import PlayerAgent
from agents.heuristic_agent import HeuristicAgent

def run_single_vs_game(seed=0):
    if seed == 0:
        rng = random.Random()
    else:
        rng = random.Random(seed)
    board = Board(size=9)
    # agent1 = PlayerAgent(1, "Fin")
    agent1 = HeuristicAgent(1, depth=4, rng=rng)
    agent2 = HeuristicAgent(-1, depth=4, rng=rng)

    game = Game(board, agent1, agent2)
    winner = game.play(verbose=True)
    print(f"Game Over. Result: {winner}")

if __name__ == "__main__":
    run_single_vs_game()