from enum import Enum
from random import choice
import os
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.panel import Panel
from rich import print
from rich.console import Console
from rich.spinner import Spinner
import time
from rich.live import Live


def rock_paper_scissor(name):

    # print(name)

    def run_game():
        console = Console()
        console.print()

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        end_loop = True
        while end_loop:
            menu = "Enter...\n1 for Rock\n2 for Paper or\n3 for Scissors"

            console.print(
                Panel.fit(
                    menu,
                    title="Please Select an Option",
                    style="bold green",
                    border_style="bold magenta",
                    padding=(1, 2),
                ),
                new_line_start=True,
            )

            user_choice = input("\nYour choice: ")

            if user_choice not in ["1", "2", "3"]:
                console.print("\nYou must enter 1,2 or 3\n", style="red bold on black")
                continue
            else:
                end_loop = False

            entered_choice = int(user_choice)
            computer_choice = int(choice("123"))

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
            style = (
                "blue"
                if "You Win" in check_winner
                else "red" if "You loose" in check_winner else ""
            )
            console.print(check_winner, style=style)

            while True:
                show = "\nWanna play again?\nY for Yes or\nQ to Quit"
                console.print(
                    Panel.fit(
                        show,
                        title="Please Select an Option",
                        style="bold blue",
                        border_style="yellow",
                        padding=(0, 1),
                    ),
                    new_line_start=True,
                )
                play_again = input("\nYour choice : ")
                if play_again.lower() not in ["y", "q"]:
                    console.print(
                        "\nYou must enter the above choices.", style="red bold on black"
                    )
                    continue
                else:
                    break

            if play_again.lower() == "y":
                os.system("cls" if os.name == "nt" else "clear")
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
        # print("\n")
        # spinner = Spinner("aesthetic", text="Processing...")
        # with Live(spinner, refresh_per_second=3):
        #     time.sleep(5)

        run_game()
