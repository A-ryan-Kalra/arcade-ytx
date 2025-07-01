import os
import random
from rich import print
from rich.console import Console
from rich.markdown import Markdown

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_running = True
winner = None
player = "X"
console = Console()
player1_win = 0
player2_win = 0
computer_win = 0
total_game = 0
opponent = None
last_opponent = None


def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    console.print(
        board[0]
        + " [bold cyan]|[/bold cyan] "
        + board[1]
        + " [bold cyan]|[/bold cyan] "
        + board[2],
        style="bold green",
    )
    console.print("----------", style="bold cyan")
    console.print(
        board[3]
        + " [bold cyan]|[/bold cyan] "
        + board[4]
        + " [bold cyan]|[/bold cyan] "
        + board[5],
        style="bold green",
    )
    console.print("----------", style="bold cyan")
    console.print(
        board[6]
        + " [bold cyan]|[/bold cyan] "
        + board[7]
        + " [bold cyan]|[/bold cyan] "
        + board[8],
        style="bold green",
    )


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
    global game_running, total_game, player1_win, player2_win, computer_win, player
    if check_horizontal(board) or check_diagonal(board) or check_vertical(board):
        console.print(f"\nWinner is player {player}\n", style="bold i blue")
        game_running = False
        total_game += 1
        if player == "X":
            player1_win += 1
        elif player == "O" and opponent == "player":
            player2_win += 1
        elif player == "O" and opponent == "computer":
            computer_win += 1
        player = "X"

        return True


def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def check_tie(board):
    global game_running, total_game
    if "-" not in board:
        # game_running = False
        print_board(board)
        print("\nIt's a tie!\n")
        total_game += 1
        return True


def computer_choice(board):
    while player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = player
            if check_winner(board):
                break
            switch_player()


def tic_tac_toe():
    global game_running, board, winner

    def run_game(board):
        global game_running, winner, player, console, player1_win, player2_win, computer_win, total_game, opponent, last_opponent

        while True:
            play_again = input(
                f"\nHello player {player},\nPress 1 to play against Player\nPress 2 to play against Computer\nor Press 3 to Exit: "
            )

            if play_again not in ["1", "2", "3"]:
                print("\nPlease choose (1 - 3): ")
                continue
            elif play_again == "1":
                opponent = "player"
                break

            elif play_again == "2":
                opponent = "computer"
                break
            elif play_again == "3":
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                game_running = True
                winner = None
                player = "X"
                console = Console()
                player1_win = 0
                player2_win = 0
                computer_win = 0
                total_game = 0
                opponent = None
                last_opponent = None
                return
        if last_opponent != opponent:
            player1_win = 0
            player2_win = 0
            total_game = 0

        last_opponent = opponent

        while game_running:
            print_board(board)
            enter_choice(board)
            if check_winner(board):
                break
            if check_tie(board):
                break
            switch_player()
            if opponent == "computer":
                computer_choice(board)

        MARKDOWN = f"""\n
> Player X Win: {player1_win}\\
> Player O Win: {player2_win if opponent=='player' else computer_win}\\
> Game Count: {total_game}\n
            """
        md = Markdown(MARKDOWN)
        console.print(md)

        while True:
            play_again = input("\nWanna play again? (y/n) ")
            if play_again not in ["y", "n"]:
                print("\nPlease choose (y/n): ")
                continue
            elif play_again == "y":
                game_running = True
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                # opponent = None
                winner = None
                os.system("cls" if os.name == "nt" else "clear")

                run_game(board)
                return
            else:
                board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                game_running = True
                winner = None
                player = "X"
                console = Console()
                player1_win = 0
                player2_win = 0
                computer_win = 0
                total_game = 0
                opponent = None
                last_opponent = None
                return

    return run_game


if __name__ == "__main__":
    exc_game = tic_tac_toe()
    exc_game(board)
