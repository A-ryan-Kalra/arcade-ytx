from enum import Enum
from random import choice
import os
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.panel import Panel
from rich import print
from rich.console import Console
import time


def rock_paper_scissor(name):

    print(name)

    def run_game():
        console = Console()

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        end_loop = True
        while end_loop:
            menu = "Enter...\n1 for Rock\n2 for Paper or\n3 for Scissors"

            print(
                Panel.fit(
                    menu,
                    title="Please Select an Option",
                    style="bold green",
                    border_style="magenta",
                    padding=(1, 2),
                )
            )

            user_choice = input("\nYour choice: ")
            # user_choice = input(
            #     "\nEnter...\n1 for Rock\n2 for Paper or\n3 for Scissors\n\n"
            # )

            if user_choice not in ["1", "2", "3"]:
                print("\nYou must enter 1,2 or 3\n")
                continue
            else:
                end_loop = False

            entered_choice = int(user_choice)
            computer_choice = int(choice("123"))
            # print(computer_choice)

            console.print(
                f"\nYou chose [cyan]{RPS(entered_choice).name}[/cyan]\nComputer chose [magenta]{RPS(computer_choice).name}[/magenta]"
            )

            def is_match() -> str:
                if entered_choice == computer_choice:
                    return "Tie Game!"
                elif entered_choice == 1 and computer_choice == 3:
                    return "You Win 🎉"
                elif entered_choice == 2 and computer_choice == 1:
                    return "You Win 🎉"
                elif entered_choice == 3 and computer_choice == 2:
                    return "You Win 🎉"
                else:
                    return "You loose 🥲"

            check_winner = is_match()

            print(check_winner)

            while True:
                play_again = input("\nWanna play again?\nY for Yes or\nQ to Quit\n\n")
                if play_again.lower() not in ["y", "q"]:
                    print("\nYou must enter the above choices.")
                    continue
                else:
                    break

            if play_again.lower() == "y":
                # os.system("cls" if os.name == "nt" else "clear")
                run_game()
            else:
                # os.system("cls" if os.name == "nt" else "clear")
                return

    return run_game


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Game Description")
    parser.add_argument(
        "-n", "--name", metavar="name", required=False, help="Enter Name"
    )
    args = parser.parse_args()

    run_game = rock_paper_scissor("Player_One" if args.name is None else args.name)

    if __name__ == "__main__":
        run_game()
