#pragma once

#include <cstdint>

#include "constants.hpp"
#include "board/board.hpp"

class Agent
{
public:
    Agent(int8_t player);
    virtual ~Agent() = default;
            
    virtual std::array<int8_t, 2> get_move(Board board) = 0;

protected:
    int8_t player;
};