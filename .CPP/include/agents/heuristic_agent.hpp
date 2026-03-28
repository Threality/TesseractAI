#pragma once

#include <random>
#include <unordered_map>
#include <vector>

#include "agents/agent.hpp"

class HeuristicAgent : public Agent
{
public:
    HeuristicAgent(int8_t player, std::mt19937 rng, int8_t max_depth = 3);

    std::array<int8_t, 2> get_move(Board board) override;

private:
    int8_t max_depth;
    std::mt19937 rng;
    std::unordered_map<int64_t, int32_t> transposition_table {};
    std::vector<std::array<int8_t, 2>> good_moves;
    int32_t window_size = 50;
    int32_t extra_depth_requirement = 50000;
    int8_t extra_depth_limit = 2;
};