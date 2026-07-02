import math

def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("-" * 9)

def winner(board):
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in lines:
        a, b, c = line
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "Tie"
    return None

def minimax(board, depth, is_maximizing):
    result = winner(board)
    if result == "O":
        return 10 - depth
    if result == "X":
        return depth - 10
    if result == "Tie":
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(board, depth+1, False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(board, depth+1, True))
                board[i] = " "
        return best

def best_move(board):
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_val = minimax(board, 0, False)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def main():
    board = [" "] * 9
    print("You are X, AI is O. Positions numbered 0-8.")
    print_board(board)

    while True:
        result = winner(board)
        if result:
            print("Tie!" if result == "Tie" else f"{result} wins!")
            break

        move = int(input("Your move (0-8): "))
        if board[move] != " ":
            print("Invalid move.")
            continue
        board[move] = "X"

        result = winner(board)
        if result:
            print_board(board)
            print("Tie!" if result == "Tie" else f"{result} wins!")
            break

        ai_move = best_move(board)
        board[ai_move] = "O"
        print_board(board)

if __name__ == "__main__":
    main()
