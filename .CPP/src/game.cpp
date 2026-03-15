#include <iostream>

#include "game.h"

Game::Game(Board& board, Agent* a1, Agent* a2)
    : board(board), agent1(a1), agent2(a2)
{
}

int Game::play(bool verbose)
{
    if (verbose)
        std::cout << "Game Starting..." << std::endl;
    return 0;
}