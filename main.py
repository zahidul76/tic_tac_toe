import tkinter as tk
from tkinter import messagebox


def print_board(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i + 3]))
        print("-----")


def check_winner(board, player):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def check_tie(board):
    return " " not in board


def on_button_click(button, position):
    global current_player

    if board[position] == ' ':
        board[position] = current_player
        button.config(text=current_player)

        if check_winner(board, current_player):
            messagebox.showinfo("Game Over", f"Congratulations! {current_player} wins!")
            window.quit()
        elif check_tie(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            window.quit()
        else:
            current_player = 'O' if current_player == 'X' else 'X'


def create_board_buttons():
    buttons = []
    for i in range(9):
        row, col = divmod(i, 3)
        button = tk.Button(window, text=" ", font=('normal', 20), width=6, height=3,
                           command=lambda pos=i: on_button_click(buttons[pos], pos))
        button.grid(row=row, column=col)
        buttons.append(button)
    return buttons


def main():
    global board, current_player, window

    board = [' ' for _ in range(9)]
    current_player = 'X'

    window = tk.Tk()
    window.title("Tic Tac Toe")

    buttons = create_board_buttons()

    window.mainloop()


if __name__ == "__main__":
    main()
