from random import choice
from rich.panel import Panel
from rich import print
from rich.console import Console
from rich.align import Align


def guess_number():

    player_win = 0
    computer_win = 0
    total_game = 0
    winning_ratio = 0

    def run_game():
        nonlocal computer_win, player_win, total_game, winning_ratio

        end_loop = True
        while end_loop:
            user_choice = input(f"\nGuess which number I'm thinking of... 1,2 or 3\n\n")
            if user_choice not in ["1", "2", "3"]:
                print("\nYou must enter 1,2 or 3")
                continue
            else:
                break

        entered_choice = int(user_choice)
        computer_choice = int(choice("123"))

        print(
            f"\nHey , you chose {entered_choice}\nI was thinking about the number {computer_choice}"
        )

        if entered_choice == computer_choice:
            player_win += 1
            print("\nYou Win 🎉\n")
        else:
            computer_win += 1
            print("You Loose 🥲")
            total_game += 1
            winning_ratio = f"{player_win/total_game:.2%}"

        end_loop = True
        while end_loop:
            play_again = input("\nWanna play again?\nY for Yes or\nQ to Quit\n")
            # print(show)

            if play_again.lower() not in ["y", "q"]:
                print("\nYou must enter the above choices\n")
                continue
            else:
                end_loop = False

        if play_again.lower() == "y":
            run_game()
        else:
            return

    return run_game


if __name__ == "__main__":
    play_game = guess_number()
    play_game()
