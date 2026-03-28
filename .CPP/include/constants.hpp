#pragma once

#include <array>
#include <cstdint>

struct Direction
{
    int8_t x, y, z;
};

struct Move
{
    int8_t x, y, z;
};

constexpr std::array<Direction, 13> directions = {{
    {1, 0, 0},   // X-axis
    {0, 1, 0},   // Y-axis
    {0, 0, 1},   // Z-axis

    {1, 1, 0},   // XY plane diagonal
    {1, -1, 0},

    {1, 0, 1},   // XZ plane diagonal
    {1, 0, -1},

    {0, 1, 1},   // YZ plane diagonal
    {0, 1, -1},

    {1, 1, 1},   // Space diagonals
    {1, 1, -1},
    {1, -1, 1},
    {1, -1, -1}
}};