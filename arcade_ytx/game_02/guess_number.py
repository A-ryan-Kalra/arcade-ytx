from random import choice
from rich.panel import Panel
from rich import print
from rich.console import Console
from rich.align import Align
import os
from rich.markdown import Markdown


def guess_number():

    player_win = 0
    computer_win = 0
    total_game = 0
    winning_ratio = 0
    console = Console()

    def run_game():
        nonlocal computer_win, player_win, total_game, winning_ratio

        end_loop = True
        while end_loop:
            menu = f"\nGuess which number I'm thinking of... 1,2 or 3\n"

            console.print(
                Panel.fit(
                    menu,
                    title="Enter number between (1 - 3)",
                    style="bold green",
                    border_style="bold magenta",
                    # padding=(1, 2),
                ),
                new_line_start=True,
            )

            user_choice = input("\nYour choice: ")
            if user_choice not in ["1", "2", "3"]:
                console.print("\nYou must enter 1,2 or 3", style="red bold on black")
                continue
            else:
                break

        entered_choice = int(user_choice)
        computer_choice = int(choice("123"))

        print(
            f"\nHey, [cyan]you chose {entered_choice}[/cyan]\n[magenta]I was thinking about the number {computer_choice}[/magenta]"
        )

        if entered_choice == computer_choice:
            player_win += 1
            console.print("\nYou Win 🎉\n", style="yellow")
        else:
            computer_win += 1
            console.print("You Loose 🥲", style="red")

        total_game += 1
        winning_ratio = f"{player_win/total_game:.2%}"

        MARKDOWN = f"""\n
> Total Win: {player_win}\\
> Winning Ratio: {winning_ratio}\\
> Game Count: {total_game}\n
            """
        md = Markdown(MARKDOWN)
        console.print(md)

        end_loop = True
        while end_loop:
            show = "\nWanna play again?\nY for Yes or\nQ to Quit\n"
            console.print(
                Panel.fit(
                    show,
                    title="Please Select an Option",
                    style="bold #FFa0CB",
                    border_style="yellow",
                    padding=(0, 1),
                ),
                new_line_start=True,
            )

            play_again = input("\nYour choice : ")

            if play_again.lower() not in ["y", "q"]:
                console.print(
                    "\nYou must enter the given choices",
                    style="red bold on black underline",
                )
                continue
            else:
                end_loop = False

        if play_again.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            run_game()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            return

    return run_game


if __name__ == "__main__":
    play_game = guess_number()
    play_game()
