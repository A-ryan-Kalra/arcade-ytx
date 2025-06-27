from bank_account import *
from rich.panel import Panel
from rich import print
from rich.console import Console


def run_bank_account():
    while end_loop:
        menu = "\n1 For Savings Account\n\n2 For Current Account"
        console.print(
            Panel.fit(
                menu,
                title="Please choose account",
                style="bold green",
                border_style="bold magenta",
                padding=(0, 1),
            ),
            new_line_start=True,
        )
        user_choice = input("\nYour choice: ")

        if user_choice not in ["1", "2"]:
            console.print(
                "\nYou must enter 1 or 2\n", style="red bold on black underline"
            )
            continue
        else:
            break
    console.print("\nPlease enter your name", style="bold magenta")
    user_name = input()
    console.print(
        "\nPlease enter the intial amount you want to deposit", style="bold yellow"
    )

    initial_amount = input()

    while not initial_amount.isdigit():
        console.print(
            "Invalid input. Please enter a number: ", style="bold red on black"
        )
        initial_amount = input()

    if int(user_choice) == 1:
        SavingsAccount(user_name, int(initial_amount))
    elif int(user_choice) == 2:
        CurrentAccount(user_name, int(initial_amount))


if __name__ == "__main__":
    end_loop = True
    console = Console()
    run_bank_account()
    # aryan = CurrentAccount("Aryan Kalra", 1221)
    # shubham = SavingsAccount("Shubham Kalra", 300)
    # aryan.show_balance()
    # aryan.deposit(2000)
    # shubham.deposit(2000)
    # aryan.show_balance()
    # aryan.withdraw_amount(2000)
    # aryan.withdraw_amount(2000)
    # aryan.transfer_amount(200, shubham)
    # aryan.withdraw_amount(2341)
