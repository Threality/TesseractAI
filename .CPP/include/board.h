#pragma once

#include <array>
#include <cstdint>

#include "constants.h"

class Board
{
public:
    static constexpr int SIZE_X = 9;
    static constexpr int SIZE_Y = 9;
    static constexpr int SIZE_Z = 9;

    Move apply_move(const int8_t& x, const int8_t& z, const int8_t& player);
    bool check_winner(const Move& move, const int8_t& player);
    bool is_column_full(const int8_t& x, const int8_t& z);
    void reset();

private:
    std::array<std::array<std::array<int, SIZE_Z>, SIZE_Y>, SIZE_X> board{};
};