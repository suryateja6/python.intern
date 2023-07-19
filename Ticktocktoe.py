import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  
            return True
        if all(board[j][i] == player for j in range(3)):  
            return True
    if all(board[i][i] == player for i in range(3)):     
        return True
    if all(board[i][2-i] == player for i in range(3)):    
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def get_computer_move(board):
    return random.choice(get_available_moves(board))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    while True:
        print_board(board)
        current_player = players[player_index]

        if is_board_full(board):
            print("It's a tie!")
            break

        if current_player == "X":
            move = input("Player X, enter your move (row and column, e.g., 1 1 for the top-left cell): ")
            row, col = map(int, move.split())
        else:
            row, col = get_computer_move(board)

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            player_index = 1 - player_index  
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
