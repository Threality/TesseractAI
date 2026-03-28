#pragma once

#include "board/board.hpp"
#include "agents/agent.hpp"

class Game
{
public:
    Game(Board& board, Agent* a1, Agent* a2);
    int play(bool verbose);
private:
    Board& board;
    Agent* agent1;
    Agent* agent2;
};