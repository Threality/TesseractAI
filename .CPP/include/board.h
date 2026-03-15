#pragma once

class Board
{
public:
    Board();
    bool make_move(int x, int y, int z);
private:
    int grid[9][9][9];
};