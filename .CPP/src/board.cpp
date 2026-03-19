#include <cstdint>
#include <stdexcept>

#include "board.h"
#include "constants.h"

#pragma region Game

Move Board::apply_move(const int8_t& x, const int8_t& z, const int8_t& player)
{
    for (int i = 0; i < SIZE_Y;  i++)
    {
        if (board[x][i][z] == 0)
        {
            board[x][i][z] = player;
            return {x, i, z};
        }
    }

    throw std::runtime_error("Played an invalid move!");
}

bool Board::check_winner(const Move& move, const int8_t& player)
{
    int8_t nx = move.x;
    int8_t ny = move.y;
    int8_t nz = move.z;
    int8_t count = 0;

    for (const auto& dir : directions)
    {
        // Move to one end of the line
        while (0 <= nx < SIZE_X && 0 <= ny < SIZE_Y && 0 <= nz < SIZE_Z && board[nx][ny][nz] == player)
        {
            nx -= dir.x;
            ny -= dir.y;
            nz -= dir.z;
            count++;
        }

        // Go to the other end
        nx = move.x + dir.x;
        ny = move.y + dir.y;
        nz = move.z + dir.z;
        while (0 <= nx < SIZE_X && 0 <= ny < SIZE_Y && 0 <= nz < SIZE_Z && board[nx][ny][nz] == player)
        {
            nx -= dir.x;
            ny -= dir.y;
            nz -= dir.z;
            count++;
        }

        // Check for a win
        if (count >= 5)
        {
            return true;
        }
    }
    return false;
}

#pragma region Utilities

bool Board::is_column_full(const int8_t& x, const int8_t& z)
{
    return board[x][SIZE_Y - 1][z] != 0;
}

void Board::reset()
{
    board = {};
}