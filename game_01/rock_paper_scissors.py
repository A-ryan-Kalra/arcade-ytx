from enum import Enum
from random import choice
import os
from rich.panel import Panel
from rich import print
from rich.console import Console
from rich.spinner import Spinner
import time
from rich.markdown import Markdown
from rich.align import Align


def rock_paper_scissor(name):

    # print(name)
    player_win = 0
    computer_win = 0
    total_game = 0
    winning_ratio = 0

    def run_game():
        nonlocal player_win, computer_win, total_game, winning_ratio, name

        console = Console()

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
                console.print(
                    "\nYou must enter 1,2 or 3\n", style="red bold on black underline"
                )
                continue
            else:
                end_loop = False

            entered_choice = int(user_choice)
            computer_choice = int(choice("123"))

            console.print(
                f"\nYou chose [cyan]{RPS(entered_choice).name}[/cyan]\nComputer chose [magenta]{RPS(computer_choice).name}[/magenta]"
            )

            def is_match() -> str:
                nonlocal player_win, computer_win

                if entered_choice == computer_choice:
                    return "Tie Game!"
                elif entered_choice == 1 and computer_choice == 3:
                    player_win += 1
                    return "You Win 🎉"
                elif entered_choice == 2 and computer_choice == 1:
                    player_win += 1
                    return "You Win 🎉"
                elif entered_choice == 3 and computer_choice == 2:
                    player_win += 1
                    return "You Win 🎉"
                else:
                    computer_win += 1
                    return "You loose 🥲"

            check_winner = is_match()
            total_game += 1
            winning_ratio = f"{player_win/total_game:.2%}"

            style = (
                "blue"
                if "You Win" in check_winner
                else "red" if "You loose" in check_winner else ""
            )
            console.print(check_winner, style=style)

            MARKDOWN = f"""\n
> Total Win: {player_win}\\
> Winning Ratio: {winning_ratio}\\
> Game Count: {total_game}\n
            """
            md = Markdown(MARKDOWN)
            console.print(md)
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
                        "\nYou must enter the above choices.",
                        style="red bold on black underline",
                    )
                    continue
                else:
                    break

            if play_again.lower() == "y":
                os.system("cls" if os.name == "nt" else "clear")
                run_game()
            else:
                os.system("cls" if os.name == "nt" else "clear")
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
    # print("\n")
    # spinner = Spinner("aesthetic", text="Processing...")
    # with Live(spinner, refresh_per_second=3):
    #     time.sleep(5)
    run_game()
