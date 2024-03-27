def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Enter row (0, 1, 2) for player {}: ".format(player)))
        col = int(input("Enter column (0, 1, 2) for player {}: ".format(player)))

        if board[row][col] != ' ':
            print("That position is already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board):
            print("Player {} wins!".format(player))
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

tic_tac_toe()
