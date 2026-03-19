#include <iostream>

#include "board.h"
#include "agent.h"
#include "game.h"

void run_single_game()
{
    Board board;

    Agent agent1(1);
    Agent agent2(-1);

    Game game(board, &agent1, &agent2);
    int winner = game.play(true);

    std::cout << "Game Over. Result: " << winner << std::endl;
}

int main()
{
    run_single_game();
}