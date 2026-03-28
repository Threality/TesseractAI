#include <random>
#include <limits>
#include <stdexcept>
#include <algorithm>

#include "agents/heuristic_agent.hpp"

HeuristicAgent::HeuristicAgent(int8_t player, std::mt19937 rng, int8_t max_depth)
    : Agent(player), max_depth(max_depth), rng(rng), good_moves(max_depth + 1)
    {}


std::array<int8_t, 2> HeuristicAgent::get_move(Board board)
{
    std::array<int8_t, 2> best_move = {-1, -1};
    bool is_maximising = player == 1;
    int32_t previous_score = 0;

    double alpha, beta;
    for (int8_t current_search_depth = 1; current_search_depth <= max_depth; current_search_depth++)
    {
        if (current_search_depth == 1)
        {
            alpha = -std::numeric_limits<double>::infinity();
            beta = std::numeric_limits<double>::infinity();
        }
        else
        {
            alpha = previous_score - window_size;
            beta = previous_score + window_size;
        }

        while (true)
        {
            double best_score;
            if (is_maximising)
            {
                best_score = -std::numeric_limits<double>::infinity();
            }
            else
            {
                best_score = std::numeric_limits<double>::infinity();
            }

            double start_alpha = alpha;
            double start_beta = beta;

            auto moves = board.get_legal_moves();
            if (moves.size() == 0)
            {
                throw std::runtime_error("Called 'get_move' with no available moves");
            }

            // Sort the moves
            std::uniform_real_distribution<double> dist(0.0, 0.1);

            std::vector<std::pair<std::array<int8_t ,2>, double>> scored_moves;
            scored_moves.reserve(moves.size());

            for (const std::array<int8_t, 2>& m : moves)
            {
                double score = board.score_move_guess(m, player);
                scored_moves.emplace_back(m, score);
            }

            std::sort(scored_moves.begin(), scored_moves.end(),
                [](const auto& a, const auto& b)
                {
                    return a.second > b.second;
                }
            );

            for (size_t i = 0; i < moves.size(); i++)
            {
                moves[i] = scored_moves[i].first;
            }

            auto& current_depth_best_move = moves[0];

            // if (board.current_hash)
        }
    }
}