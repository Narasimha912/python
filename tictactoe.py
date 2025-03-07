def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}, enter your move (row and column: 1 1 for center): ")
        
        try:
            row, col = map(int, input().split())
            if board[row - 1][col - 1] != " ":
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 1 and 3.")
            continue

        board[row - 1][col - 1] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins! 🎉")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break
        
        turn += 1

tic_tac_toe()
