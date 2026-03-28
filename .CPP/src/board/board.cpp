#include <cstdint>
#include <stdexcept>
#include <iostream>
#include <random>

#include "board/board.hpp"
#include "constants.hpp"

#pragma region Game

Board::Board()
{
    std::mt19937_64 rng(std::random_device{}());

    for (int8_t x = 0; x < SIZE_X; x++)
    {
        for (int8_t y = 0; y < SIZE_Y; y++)
        {
            for (int8_t z = 0; z < SIZE_Z; z++)
            {
                zobrist_table[x][y][z][0] = rng();
                zobrist_table[x][y][z][1] = rng();
            }
        }
    }
}

Move Board::apply_move(const int8_t& x, const int8_t& z, const int8_t& player)
{
    for (int8_t i = 0; i < SIZE_Y;  i++)
    {
        if (board[x][i][z] == 0)
        {
            board[x][i][z] = player;
            return {x, i, z};
        }
    }

    throw std::runtime_error("Played an invalid move!");
}

const bool Board::check_winner(const Move& move, const int8_t& player)
{
    int8_t nx = move.x;
    int8_t ny = move.y;
    int8_t nz = move.z;
    int8_t count = 0;

    for (const auto& dir : directions)
    {
        // Move to one end of the line
        while (is_within_bounds(nx, ny, nz) && board[nx][ny][nz] == player)
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
        while (is_within_bounds(nx, ny, nz) && board[nx][ny][nz] == player)
        {
            nx += dir.x;
            ny += dir.y;
            nz += dir.z;
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

const bool Board::is_column_full(const int8_t& x, const int8_t& z)
{
    return board[x][SIZE_Y - 1][z] != 0;
}

void Board::reset()
{
    board = {};
}

const bool Board::is_within_bounds(const Move& move)
{
    return is_within_bounds(move.x, move.y, move.z);
}

const bool Board::is_within_bounds(const int8_t& x, const int8_t& y, const int8_t& z)
{
    if (x < 0 || x >= SIZE_X) return false;
    if (y < 0 || y >= SIZE_Y) return false;
    if (z < 0 || z >= SIZE_Z) return false;
    return true;
}

const void Board::print_board()
{
    for (int y = SIZE_Y - 1; y >= 0; y--)
    {
        std::cout << "Layer y = " << y << "\n";

        // Print x-axis
        std::cout << "  ";
        for (int x = 0; x < SIZE_X; x++)
        {
            std::cout << x << " ";
        }
        std::cout << "\n";

        for (int z = 0; z < SIZE_Z; z++)
        {
            // Print z-axis label
            std::cout << z << " ";

            for (int x = 0; x < SIZE_X; x++)
            {
                int cell = board[x][y][z];

                char c;
                if (cell == 1) c = 'X';
                else if (cell == -1) c = 'O';
                else c = '.';

                std::cout << c << " ";
            }

            std::cout << "\n";
        }

        std::cout << "\n";
    }
}

#pragma region AI Tools

const std::vector<std::array<int8_t, 2>> Board::get_legal_moves()
{
    std::vector<std::array<int8_t, 2>> out = {};
    for (int8_t x = 0; x < SIZE_X; x++)
    {
        for (int8_t z = 0; z < SIZE_Z; z++)
        {
            out.push_back({x, z});
        }
    }

    return out;
}

const float Board::score_move_guess(std::array<int8_t, 2>, int8_t player)
{
    return 0.0;
}