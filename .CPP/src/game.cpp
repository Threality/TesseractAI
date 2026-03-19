#include <iostream>

#include "game.h"

Game::Game(Board& board, Agent* a1, Agent* a2)
    : board(board), agent1(a1), agent2(a2) {}

int Game::play(bool verbose)
{
    if (verbose)
        std::cout << "Game Starting..." << std::endl;
    board.reset();
    int8_t cur_player = 1;

    while (true)
    {
        Agent* active_agent = (cur_player == 1) ? agent1 : agent2;
        std::array<int8_t, 2> move = active_agent->get_move(board);

        Move final_move = board.apply_move(move[0], move[1], cur_player);

        if (board.check_winner(final_move, cur_player))
        {
            return cur_player;
        }

        cur_player *= -1;
    }
}