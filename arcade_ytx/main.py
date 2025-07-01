from .game_01.rock_paper_scissors import rock_paper_scissor
from .game_02.guess_number import guess_number
from .game_03.tic_tac_toe import tic_tac_toe
from .game_04.main import (
    bank_account_main,
    read_data,
    SavingsAccount,
    CurrentAccount,
    user_data,
)
import pyfiglet
from rich.console import Console
from rich.panel import Panel
import os
import sys

console = Console()
font = pyfiglet.figlet_format(
    "........... Welcome To Arcade-YTX ...........", font="starwars"
)
developer_name = pyfiglet.figlet_format("By Aryan Kalra", font="digital")


def show_menu():
    while True:
        menu = "\n1. Rock Paper Scissors\n\n2. Guess Number\n\n3. Tic Tac Toe\n\n4. Create Bank Account"

        console.print(
            Panel(
                menu,
                title=f"Choose a number to proceed with the game!",
                subtitle="Press 5 to Exit(🚪)",
                style="bold green",
                border_style="bold #e122f2",
                padding=(0, 1),
                width=50,
            ),
            new_line_start=True,
            justify="left",
        )
        while True:
            try:
                user_choice = int(input("\nYour choice: "))
                if user_choice not in range(1, 10):
                    console.print("You must enter (1 - 5)", style="bold red on black")
                    continue
                else:
                    break
            except:
                console.print("You must enter (1 - 5)", style="bold red on black")

        entered_choice = int(user_choice)

        if entered_choice == 1:
            os.system("cls" if os.name == "nt" else "clear")
            run = rock_paper_scissor("")
            run()
        elif entered_choice == 2:
            os.system("cls" if os.name == "nt" else "clear")
            run = guess_number()
            run()
            print("entered_choice, account, store_details")
        elif entered_choice == 3:
            os.system("cls" if os.name == "nt" else "clear")
            board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
            run = tic_tac_toe()
            run(board)
            os.system("cls" if os.name == "nt" else "clear")

        elif entered_choice == 4:
            print("entered_choice, account, store_details")
            all_data = (
                read_data("user-list") if type(read_data("user-list")) is dict else {}
            )

            for item in all_data.values():
                if item.get("type") == "Savings":
                    account = SavingsAccount(
                        item.get("name"), float(item.get("balance"))
                    )
                else:
                    account = CurrentAccount(
                        item.get("name"), float(item.get("balance"))
                    )
                types = 1 if account.type == "Savings" else 2
                user_data[item.get("name") + str(types)] = account
            os.system("cls" if os.name == "nt" else "clear")

            exec_bank_account = bank_account_main(user_data, all_data)
            exec_bank_account()
            os.system("cls" if os.name == "nt" else "clear")
        elif entered_choice == 5:
            break
        else:
            console.print(f"You must enter (1 - 9)", style="bold red on black")


def run_game():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        console.print(f"[green bold]{font}[/green bold]\n")
        console.print(
            f"[bold yellow]{developer_name}[/bold yellow]\n", justify="center"
        )
        show_menu()
    except Exception as error:
        console.print(f"\nError occurred at: \n{error}\n", style="bold red on black")
        sys.exit()


if __name__ == "__main__":
    run_game()
