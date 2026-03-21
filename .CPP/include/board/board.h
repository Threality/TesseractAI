#pragma once

#include <array>
#include <vector>
#include <cstdint>

#include "constants.h"

class Board
{
public:
    static constexpr int SIZE_X = 9;
    static constexpr int SIZE_Y = 9;
    static constexpr int SIZE_Z = 9;

    Move apply_move(const int8_t& x, const int8_t& z, const int8_t& player);
    const bool check_winner(const Move& move, const int8_t& player);
    const bool is_column_full(const int8_t& x, const int8_t& z);
    const bool is_within_bounds(const Move& move);
    const bool is_within_bounds(const int8_t& x, const int8_t& y, const int8_t& z);
    const std::vector<std::array<int8_t, 2>> get_legal_moves();
    const void print_board();
    void reset();

private:
    std::array<std::array<std::array<int8_t, SIZE_Z>, SIZE_Y>, SIZE_X> board{};
};