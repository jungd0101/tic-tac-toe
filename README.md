# Minimax Tic-Tac-Toe AI

A terminal-based Tic-Tac-Toe game where you play against an unbeatable AI powered by the minimax algorithm.

## How It Works
The AI uses **minimax**, a recursive adversarial search algorithm that explores the entire game tree from the current board state. For every possible move, it simulates all subsequent moves by both players down to every possible game-ending state, scoring wins, losses, and ties. It then picks the move that maximizes its own guaranteed outcome, assuming the opponent also plays optimally.

Because Tic-Tac-Toe's game tree is small enough to fully explore, this guarantees optimal play — the AI can never lose. The best a human opponent can achieve is a tie.

## Requirements
No external dependencies — pure Python standard library.

## Usage
```bash
python tictactoe_ai.py
```

You play as `X`, the AI plays as `O`. Enter a number 0-8 corresponding to the board position:

## Notes
- Minimax is a brute-force but exhaustive algorithm — it's not machine learning, there's no training or learned weights. It recalculates the optimal move from scratch every turn by evaluating outcomes.
- This approach works cleanly for Tic-Tac-Toe because the game tree is small (at most 9! ≈ 362,880 states). Larger games (e.g. Chess) need alpha-beta pruning, depth limits, and heuristic evaluation functions to stay tractable.
