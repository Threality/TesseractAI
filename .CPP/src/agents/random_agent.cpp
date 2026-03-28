#include "agents/random_agent.hpp"

#include <stdexcept>

RandomAgent::RandomAgent(int8_t player)
    : Agent(player), rng(std::random_device{}()) {}

std::array<int8_t, 2> RandomAgent::get_move(Board board)
{
    auto moves = board.get_legal_moves();

    if (moves.empty())
    {
        throw std::runtime_error("No valid moves left");
    }

    std::uniform_int_distribution<size_t> dist(0, moves.size() - 1);
    return moves[dist(rng)];
}