import os
import random

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_running = True
winner = None
player = "X"


def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def enter_choice(board):
    while True:
        inp = input(f"\nPlayer {player}, Please enter your choice (1-9): ")

        if not (inp.isdecimal()):
            print("\nPlease enter valid number")
        elif int(inp) < 0 or int(inp) > 9:
            print("\nPlayer {player}, Please enter between (1 - 9): ")
        elif int(inp) > 0 and int(inp) <= 9 and board[int(inp) - 1] == "-":
            board[int(inp) - 1] = player
            break
        else:
            print("\nOops! this spot is already occupied. Please select another one")


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = player
        print_board(board)
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = player
        print_board(board)
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = player
        print_board(board)
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = player
        print_board(board)
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = player
        print_board(board)
        return True


def check_vertical(board):
    global winner

    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = player
        print_board(board)
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = player
        print_board(board)
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = player
        print_board(board)
        return True


def check_winner(board):
    global game_running
    if check_horizontal(board) or check_diagonal(board) or check_vertical(board):
        print(f"\nWinner is player {player}\n")
        game_running = False
        return True


def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def check_tie(board):
    global game_running
    if "-" not in board:
        game_running = False
        print_board(board)
        print("\nIt's a tie!\n")


def computer_choice(board):
    while player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = player
            check_winner(board)
            switch_player()


while game_running:
    print_board(board)
    enter_choice(board)
    if check_winner(board):
        break
    check_tie(board)
    switch_player()
    computer_choice(board)
