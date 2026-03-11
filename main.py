from core.board import Board
from core.game import Game
from agents.random_agent import RandomAgent

def run_single_vs_game():
    board = Board(size=9)
    agent1 = RandomAgent(1)
    agent2 = RandomAgent(-1)

    game = Game(board, agent1, agent2)
    winner = game.play()
    print(f"Game Over. Result: {winner}")

if __name__ == "__main__":
    run_single_vs_game()