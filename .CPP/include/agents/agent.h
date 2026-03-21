#pragma once

#include <cstdint>

#include "constants.h"
#include "board/board.h"

class Agent
{
public:
    Agent(int8_t player);
    virtual ~Agent() = default;
            
    virtual std::array<int8_t, 2> get_move(Board board) = 0;

protected:
    int8_t player;
};