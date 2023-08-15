import tkinter as tk
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

def update_ui():
    for i in range(3):
        for j in range(3):
            cell_label = board_labels[i][j]
            cell_value = board[i][j]
            cell_label.config(text=cell_value, state=tk.DISABLED if cell_value != " " else tk.NORMAL)

def on_cell_click(row, col):
    global player_index

    if board[row][col] == " ":
        board[row][col] = players[player_index]

        if check_winner(board, players[player_index]):
            winner_label.config(text=f"Player {players[player_index]} wins!", fg="green")
            for i in range(3):
                for j in range(3):
                    board_labels[i][j].config(state=tk.DISABLED)
        elif is_board_full(board):
            winner_label.config(text="It's a tie!", fg="orange")
        else:
            player_index = 1 - player_index
            update_ui()

def tic_tac_toe_ui():
    global board, players, player_index, board_labels, winner_label

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_index = 0

    root = tk.Tk()
    root.title("Colorful Tic-Tac-Toe")

    board_labels = [[None] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            board_labels[i][j] = tk.Button(root, text=" ", font=("Helvetica", 24), width=5, height=2,
                                           command=lambda i=i, j=j: on_cell_click(i, j))
            board_labels[i][j].grid(row=i, column=j)
    
    winner_label = tk.Label(root, text="", font=("Helvetica", 16), fg="black")
    winner_label.grid(row=3, columnspan=3)

    update_ui()

    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe_ui()
