#pragma once

#include <cstdint>

#include "constants.h"
#include "board.h"

class Agent
{
public:
    Agent(int player);
    virtual ~Agent() = default;
            
    virtual std::array<int8_t, 2> get_move(Board board);

protected:
    int8_t player;
};