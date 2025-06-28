from bank_account import *
from rich.panel import Panel
from rich import print
from rich.console import Console
import os
from typing import Union


def fetch_info(num, account: Union[BankAccount]):
    match num:
        case 1:
            return account.show_balance()
        case 2:
            menu = "\nPlease enter the amount you wish to deposit\n"
            console.print(menu, style="bold magenta")
            amount = float(input())
            return account.deposit(amount)
        case 3:
            menu = "\nPlease enter the amount you wish to withdraw\n"
            console.print(menu, style="bold magenta")
            amount = float(input())
            return account.withdraw_amount(amount)
        case 4:
            menu = "\nPlease enter the amount you wish to transfer\n"
            console.print(menu, style="bold magenta")
            amount = float(input())
            return account.transfer_amount(amount, account)


def run_bank_account():
    end_loop = True
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
            end_loop = False

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

    os.system("cls" if os.name == "nt" else "clear")

    if int(user_choice) == 1:
        account = SavingsAccount(user_name, int(initial_amount))
    elif int(user_choice) == 2:
        account = CurrentAccount(user_name, int(initial_amount))

    while True:
        menu = "\n1. Show Balance\t\t2. Deposit Amount\n\n3. Withdraw Amount\t4. Transfer Amount\n\n5. Exit"
        console.print(
            Panel(
                menu,
                title="Please select a number",
                style="bold green",
                border_style="bold magenta",
                padding=(0, 1),
                width=48,
            ),
            new_line_start=True,
            justify="left",
        )
        while True:
            user_choice = input("\nYour choice: ")
            if user_choice not in ["1", "2", "3", "4", "5"]:
                console.print("You must enter 1,2,3,4 or 5", style="bold red on black")
                continue
            else:
                break
        entered_choice = int(user_choice)
        # if entered_choice == 1:
        #     account.show_balance()
        # if entered_choice == 5:
        #     break
        if entered_choice >= 1 and entered_choice <= 4:
            fetch_info(entered_choice, account)
        elif entered_choice == 5:
            break
        else:
            console.print("You must enter 1,2,3or 4", style="bold red on black")


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
