#include <iostream>

#include "board/board.hpp"
#include "agents/random_agent.hpp"
#include "game.hpp"

void run_single_game()
{
    Board board;

    RandomAgent agent1(1);
    RandomAgent agent2(-1);

    Game game(board, &agent1, &agent2);
    int winner = game.play(true);

    std::cout << "Game Over. Result: " << winner << std::endl;
}

int main()
{
    run_single_game();
}