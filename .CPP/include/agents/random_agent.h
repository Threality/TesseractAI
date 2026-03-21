#pragma once

#include <random>

#include "agents/agent.h"

class RandomAgent : public Agent
{
public:
    RandomAgent(int8_t player);

    std::array<int8_t, 2> get_move(Board board) override;

private:
    std::mt19937 rng;
};