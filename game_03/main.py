from bank_account import *
from rich.panel import Panel
from rich import print
from rich.console import Console
import os
from typing import Union
from rich.table import Table
from rich.align import Align


user_data = {}


def create_user(user_name, type, initial_amount):
    if user_name not in user_data:
        if int(type) == 1:
            new_account = SavingsAccount(user_name, float(initial_amount))
        elif int(type) == 2:
            new_account = CurrentAccount(user_name, float(initial_amount))

        user_data[user_name] = new_account
        return user_data[user_name]


def get_user(user_name):
    return user_data.get(user_name)


def fetch_info(num, account: Union[BankAccount], store_details):
    os.system("cls" if os.name == "nt" else "clear")
    match num:
        case 1:
            return account.show_balance()
        case 2:
            menu = "\nPlease enter the amount you wish to deposit\n"
            console.print(menu, style="bold magenta")
            amount = float(input(f"Enter amount: "))
            return account.deposit(amount)
        case 3:
            menu = "\nPlease enter the amount you wish to withdraw\n"
            console.print(menu, style="bold magenta")
            amount = float(input(f"Enter amount: "))
            return account.withdraw_amount(amount)
        case 4:
            table = Table(title="List Of Accounts", min_width=50)
            all_acounts = [
                detail
                for detail in store_details
                if detail.get("user_name") != account.name
            ]
            if len(all_acounts) == 0:

                console.print(
                    "\nOops, you don't have anyone in your contact to transfer your amount with\n",
                    style="green bold",
                )
                console.print(
                    "Would you like to add more accounts? (y/n):  ", style="yellow bold"
                )

                while True:
                    entered_choice = input("")
                    if entered_choice.lower() not in ["y", "n"]:
                        print("\nPlease enter (y/n) \n")
                        continue
                    else:
                        break

                if entered_choice == "n":
                    return

                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    # account_create(store_details)
                    initial_amount, user_name, type = account_create(
                        store_details
                    ).values()

                    create_user(user_name, type, initial_amount)

                    # os.system("cls" if os.name == "nt" else "clear")

                    console.print(
                        "Would you like to add more accounts? (y/n):  ",
                        style="yellow bold",
                    )
                    while True:
                        add_account = input("")
                        if add_account.lower() not in ["y", "n"]:
                            print("\nPlease enter (y/n) \n")
                            continue
                        else:
                            break
                    if add_account.lower() == "n":
                        os.system("cls" if os.name == "nt" else "clear")
                        all_acounts = [
                            detail
                            for detail in store_details
                            if detail.get("user_name") != account.name
                        ]
                        break

            table.add_column("No", style="blue", justify="center")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta")
            table.add_column("Balance", style="green")

            for index, user in enumerate(all_acounts):
                table.add_row(
                    str(index + 1) + ".",
                    user.get("user_name"),
                    user.get("type"),
                    str(user.get("initial_amount")),
                )

            console.print(Align.center(table, style="bold"))
            while True:
                select_acc = int(
                    input(
                        "\nPlease select the account via number to proceed with transfer.\n"
                    )
                )
                if select_acc != 0 and select_acc <= len(all_acounts):
                    break
                else:
                    continue

            selected_user_name = all_acounts[select_acc - 1].get("user_name")
            transfer_acc = get_user(user_name=selected_user_name)

            menu = "\nPlease enter the amount you wish to transfer\n"
            console.print(menu, style="bold magenta")
            amount = float(input(f"Enter amount: "))
            os.system("cls" if os.name == "nt" else "clear")
            return account.transfer_amount(amount, transfer_acc)

        case 5:
            table = Table(title="List Of Accounts", min_width=50)
            table.add_column("No", style="blue", justify="center")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta")
            table.add_column("Balance", style="green")

            for index, user in enumerate(user_data):
                acc = get_user(user_name=user)
                table.add_row(
                    str(index + 1) + ".",
                    acc.name,
                    acc.type,
                    f"{acc.balance:.2f}",
                )
            console.print(Align.center(table, style="bold"))
            return
        case 6:
            while True:
                initial_amount, user_name, type = account_create(store_details).values()
                print("chosen", type)
                create_user(user_name, type, initial_amount)

                fetch_info(5, account, store_details)

                console.print(
                    "Would you like to add more accounts? (y/n):  ",
                    style="yellow bold",
                )

                while True:
                    create_again = input("")
                    if create_again.lower() not in ["y", "n"]:
                        print("\nPlease enter (y/n) ")
                        continue
                    else:
                        break
                if create_again == "y":
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    break


def account_create(store_details: list) -> dict:

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

    console.print("\nPlease enter name", style="bold magenta")
    user_name = input()
    console.print(
        "\nPlease enter the intial amount you want to deposit", style="bold yellow"
    )

    while True:
        try:
            initial_amount = float(input())
            break
        except ValueError:
            console.print(
                "Invalid input. Please enter a number: ", style="bold red on black"
            )
    type = "Savings" if int(user_choice) == 1 else "Current"
    store_details.append(
        {
            "initial_amount": initial_amount,
            "user_name": user_name,
            "type": type,
        }
    )
    return {
        "initial_amount": initial_amount,
        "user_name": user_name,
        "type": user_choice,
    }


def bank_account_main():
    store_details = []

    def run_bank_account():
        nonlocal store_details

        initial_amount, user_name, type = account_create(store_details).values()

        os.system("cls" if os.name == "nt" else "clear")

        if int(type) == 1:
            account = SavingsAccount(user_name, float(initial_amount))
        elif int(type) == 2:
            account = CurrentAccount(user_name, float(initial_amount))

        user_data[user_name] = account

        while True:
            menu = "\n1. Show Balance\t\t2. Deposit Amount\n\n3. Withdraw Amount\t4. Transfer Amount\n\n5. Show All Acounts\t6. Create Account\n\n7. Exit"

            console.print(
                Panel(
                    menu,
                    title=f"Hey {account.name.split(" ")[0]}, Please select a number",
                    style="bold green",
                    border_style="bold magenta",
                    padding=(0, 1),
                    width=48,
                ),
                new_line_start=True,
                justify="left",
            )
            while True:
                user_choice = int(input("\nYour choice: "))
                if user_choice not in range(1, 8):
                    console.print(
                        "You must enter 1,2,3,4,5,6 or 7", style="bold red on black"
                    )
                    continue
                else:
                    break

            entered_choice = int(user_choice)

            if entered_choice >= 1 and entered_choice <= 6:
                fetch_info(entered_choice, account, store_details)
            elif entered_choice == 7:
                break
            else:
                console.print("You must enter 1,2,3or 4", style="bold red on black")

    return run_bank_account


if __name__ == "__main__":
    end_loop = True
    console = Console()
    # try:
    exec_bank_account = bank_account_main()
    exec_bank_account()
    # except Exception as error:
    # console.print(f"\nError occurred at: \n{error}\n", style="bold red on black")
