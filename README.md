<div align="center">

  <h1 style="font-size:80px;">Tesseract</h1>
  <h3 style="font-size:30px;"> A 3D Connect-5 AI</h3>

</div>

## Overview

Tesseract is a 3D Connect-5 engine designed for experimenting with game AI techniques.
The project focuses on efficient board representation, fast move generation, and search-based agents.

It was originally created as a playground for implementing and testing different AI approaches such as heuristic evaluation, alpha-beta pruning, and eventually neural network based agents.

Currently performance is still quite limited even with the current optimisations.

## Current Features

### Game Engine
- 3D Connect-5 implementation with configurable board size
- Efficient win detection across all 3D directions
- Fast board updates using NumPy

### AI Search
- **Minimax search with Alpha-Beta pruning**
  - Reduces the number of evaluated positions by pruning branches that cannot influence the final decision

- **Transposition tables**
  - Previously evaluated board states are cached and reused to avoid redundant computation

- **Move ordering**
  - Moves are sorted using a heuristic to maximise alpha-beta pruning effectiveness

### Optimisations
- **Zobrist hashing**
  - Fast incremental board hashing used for transposition table lookups

- **Move filtering**
  - Only moves near existing tokens are considered, significantly reducing the branching factor

### Tools
- **3D board visualiser**
  - Uses matplotlib for rendering game states

- **Agent vs agent simulation**
  - Allows large batches of games to be run for testing and benchmarking

## Implementation

### Board Representation

The board is represented as a 3D NumPy array.  
Each position stores a value representing the occupying player.

This structure allows simple indexing and efficient iteration across the grid when evaluating streaks or checking win conditions.

---

### Alpha-Beta Search

The AI uses a minimax search algorithm with alpha-beta pruning.

Alpha-beta pruning works by keeping track of two bounds:

- **Alpha** – the best score the maximizing player can guarantee
- **Beta** – the best score the minimizing player can guarantee

When the algorithm determines that a branch cannot possibly influence the final decision, it stops exploring that branch.

This dramatically reduces the number of nodes evaluated and allows deeper searches.

---

### Transposition Tables

Many board states can be reached through different sequences of moves.

To avoid re-evaluating identical positions, the engine stores previously evaluated states in a **transposition table**.

Each board state is identified using a Zobrist hash and mapped to its computed evaluation.

This allows the search to reuse previous results and significantly improves performance.

---

### Zobrist Hashing

Each possible `(x, y, z, player)` combination is assigned a random 64-bit integer.

The current board hash is updated incrementally whenever a move is played or undone using XOR operations.

This makes hashing extremely fast and suitable for use during deep search.

---

### Move Filtering

Instead of considering every empty square on the board, the engine only evaluates moves within a certain radius of existing tokens.

Since useful moves in Connect-style games tend to occur near existing pieces, this reduces the branching factor without significantly impacting decision quality.

## Future Improvements

Planned improvements include:

- **Bitboard representation**
  - Replace the NumPy board with a compact bitboard representation for faster operations

- **Improved evaluation function**
  - More sophisticated scoring of board states and streak threats

- **Neural network evaluation**
  - Replace the heuristic evaluation function with a trained neural model

- **Self-play training**
  - Generate training data through large-scale agent simulations

- **Parallel search**
  - Explore multi-threaded search to further increase search depth

- **Better move ordering**
  - Improve pruning efficiency by prioritising stronger candidate moves earlier in the search