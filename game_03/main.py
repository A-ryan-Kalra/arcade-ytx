from bank_account import *
from rich.panel import Panel
from rich import print
from rich.console import Console
import os
from typing import Union
from rich.table import Table
from rich.align import Align
import sys
import os
import json

user_data = {}
combined = {}
all_data = {}


def write_data(key, value):
    combined.update({key: value})
    with open("user-details.json", "w") as of:
        json.dump(combined, of, indent=2)


def read_data(key):
    if os.path.exists("user-details.json"):
        with open("user-details.json") as of:
            try:
                combined = json.load(of)
                return combined[key]
            except Exception as error:
                # print("No data exist\nLet's create your account!")
                combined = {}


def create_user(user_name, type, initial_amount):
    if user_name + type not in user_data:
        if int(type) == 1:
            new_account = SavingsAccount(user_name, float(initial_amount))
        elif int(type) == 2:
            new_account = CurrentAccount(user_name, float(initial_amount))

    elif user_name + type in user_data:
        if user_data[user_name + type].type == type:
            raise Exception(
                "\nUser already created, please try again with another username\n"
            )
        else:
            if int(type) == 1:
                new_account = SavingsAccount(user_name, float(initial_amount))
            elif int(type) == 2:
                new_account = CurrentAccount(user_name, float(initial_amount))

    user_data[user_name + type] = new_account
    all_data[user_name + type] = new_account.to_dict()
    write_data("user-list", all_data)

    return user_data[user_name + type]


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
                or detail.get("type") != account.type
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
                    try:
                        # os.system("cls" if os.name == "nt" else "clear")
                        # account_create(store_details)
                        initial_amount, user_name, type = account_create(
                            store_details
                        ).values()
                        os.system("cls" if os.name == "nt" else "clear")
                        create_user(user_name, type, initial_amount)

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
                                or detail.get("type") != account.type
                            ]
                            break
                    except Exception as error:
                        print(error)
                        # continue

            table.add_column("No", style="blue", justify="center")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta")
            table.add_column("Balance", style="green")

            for index, user in enumerate(all_acounts):
                table.add_row(
                    str(index + 1) + ".",
                    user.get("user_name"),
                    user.get("type"),
                    f"{user.get('initial_amount'):.2f}",
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
            type = 1 if all_acounts[select_acc - 1].get("type") == "Savings" else 2
            transfer_acc = get_user(user_name=selected_user_name + str(type))

            menu = "\nPlease enter the amount you wish to transfer\n"
            console.print(menu, style="bold magenta")
            amount = float(input(f"Enter amount: "))
            os.system("cls" if os.name == "nt" else "clear")

            account.transfer_amount(amount, transfer_acc)

            for account in store_details:
                if (
                    account["user_name"] == transfer_acc.name
                    and account["type"] == transfer_acc.type
                ):
                    account["initial_amount"] = transfer_acc.balance

            return

        case 5:
            table = Table(title="List Of Accounts", min_width=50)
            table.add_column("No", style="blue", justify="center")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta")
            table.add_column("Balance", style="green")

            all_acounts = store_details

            for index, user in enumerate(all_acounts):
                table.add_row(
                    str(index + 1) + ".",
                    user.get("user_name"),
                    user.get("type"),
                    f"{user.get('initial_amount'):.2f}",
                )
            console.print(Align.center(table, style="bold"))
            return
        case 6:
            while True:
                try:
                    initial_amount, user_name, type = account_create(
                        store_details
                    ).values()

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
                except Exception as error:
                    print(error)
        case 7:
            all_acounts = [
                detail
                for detail in store_details
                if detail.get("user_name") != account.name
                or detail.get("type") != account.type
            ]

            if len(all_acounts) == 0:
                print(
                    "Oops, You don't have enough accounts,\nplease create more accounts and try again."
                )
                return account

            fetch_info(5, account, store_details=all_acounts)

            console.print(
                "\nPlease select the account via number to switch your account with\n"
            )
            while True:
                try:
                    switch_acc = int(input("\nYour choice\n")) - 1

                    if switch_acc < 0:
                        print("Please enter number only")
                except:
                    print("Please enter a valid number")
                    continue

                if switch_acc not in range(0, len(all_acounts)):
                    console.print(
                        f"\nPlease select the number between (1 - {len(all_acounts)})\n",
                        style="bold red on black",
                    )
                    continue
                else:
                    break

            get_acc = all_acounts[switch_acc]

            user_name = get_acc["user_name"]
            type = 1 if get_acc["type"] == "Savings" else 2
            account = user_data[user_name + str(type)]
            return account
        case 8:
            all_acounts = [
                detail
                for detail in store_details
                if detail.get("user_name") != account.name
                or detail.get("type") != account.type
            ]

            if len(all_acounts) == 0:
                print(
                    "Oops, You don't have enough accounts,\nplease create more accounts and try again."
                )
                return store_details
            table = Table(title="List Of Accounts", min_width=50)
            table.add_column("No", style="blue", justify="center")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta")
            table.add_column("Balance", style="green")

            for index, user in enumerate(all_acounts):
                table.add_row(
                    str(index + 1) + ".",
                    user.get("user_name"),
                    user.get("type"),
                    f"{user.get('initial_amount'):.2f}",
                )
            console.print(Align.center(table, style="bold"))
            console.print(
                "\nPlease select the account via number to delete the account\n"
            )
            while True:
                try:
                    switch_acc = int(input("\nYour choice\n")) - 1

                    if switch_acc < 0:
                        print("Please enter number only")
                except:
                    print("Please enter a valid number")
                    continue

                if switch_acc not in range(0, len(all_acounts)):
                    console.print(
                        f"\nPlease select the number between (1 - {len(all_acounts)})\n",
                        style="bold red on black",
                    )
                    continue
                else:
                    break
            get_acc = all_acounts[switch_acc]

            user_name = get_acc["user_name"]
            store_details = [
                detail for detail in store_details if detail["user_name"] != user_name
            ]
            type = 1 if get_acc["type"] == "Savings" else 2

            del user_data[user_name + str(type)]
            all_data.pop(user_name + str(type))
            write_data("user-list", all_data)
            write_data("store-data", store_details)
            return store_details


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
    user_name = input().strip()

    type = "Savings" if int(user_choice) == 1 else "Current"
    if user_name + user_choice in user_data:

        if user_data[user_name + user_choice].type == type:
            raise Exception(
                "\nUser already created, please try again with another username\n"
            )

    console.print(
        "\nPlease enter the intial amount you want to deposit", style="bold yellow"
    )

    while True:
        try:
            initial_amount = float(input().strip())
            break
        except ValueError:
            console.print(
                "Invalid input. Please enter a number: ", style="bold red on black"
            )

    store_details.append(
        {
            "initial_amount": (
                initial_amount * 1.05 if int(user_choice) == 1 else initial_amount
            ),
            "user_name": user_name,
            "type": type,
        }
    )

    write_data("store-data", store_details)

    return {
        "initial_amount": initial_amount,
        "user_name": user_name,
        "type": user_choice,
    }


def bank_account_main():
    store_details = []
    store_details = (
        read_data("store-data") if type(read_data("store-data")) is list else []
    )

    def run_bank_account():
        nonlocal store_details
        if len(user_data) == 0:
            initial_amount, user_name, type = account_create(store_details).values()

            os.system("cls" if os.name == "nt" else "clear")

            if int(type) == 1:
                account = SavingsAccount(user_name, float(initial_amount))
            elif int(type) == 2:
                account = CurrentAccount(user_name, float(initial_amount))

            user_data[user_name + type] = account
            all_data[user_name + type] = account.to_dict()
            write_data("user-list", all_data)
        else:
            table = Table(title="List Of Accounts", min_width=50)
            table.add_column("No", style="blue", justify="center")
            table.add_column("Name", style="cyan")
            table.add_column("Type", style="magenta")
            table.add_column("Balance", style="green")

            all_acounts = store_details

            for index, user in enumerate(all_acounts):
                table.add_row(
                    str(index + 1) + ".",
                    user.get("user_name"),
                    user.get("type"),
                    f"{user.get('initial_amount'):.2f}",
                )
            console.print(Align.center(table, style="bold"))

            while True:
                selec_acc = input("Your choice :")
                if selec_acc.isdigit():
                    selec_acc = int(selec_acc) - 1
                else:
                    print("That's not a valid number.")
                    continue

                if selec_acc not in range(0, len(store_details)):
                    console.print(
                        f"You must enter 1 - ({len(store_details)})",
                        style="bold red on black",
                    )
                    continue
                else:
                    break

            acc = all_acounts[selec_acc]

            if (acc["type"]) == "Savings":
                account = SavingsAccount(acc["user_name"], float(acc["initial_amount"]))
            else:
                account = CurrentAccount(acc["user_name"], float(acc["initial_amount"]))
        os.system("cls" if os.name == "nt" else "clear")

        while True:
            menu = "\n1. Show Balance\t\t2. Deposit Amount\n\n3. Withdraw Amount\t4. Transfer Amount\n\n5. Show All Accounts\t6. Create Account\n\n7. Switch Account\t8. Delete Accounts\n\n9. Exit"

            console.print(
                Panel(
                    menu,
                    title=f"Hey {account.name.split(' ')[0]}, Please select a number",
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
                if user_choice not in range(1, 10):
                    console.print(
                        "You must enter 1,2,3,4,5,6,7,8 or 9", style="bold red on black"
                    )
                    continue
                else:
                    break

            entered_choice = int(user_choice)

            if entered_choice >= 1 and entered_choice <= 6:
                fetch_info(entered_choice, account, store_details)
            elif entered_choice == 7:
                account = fetch_info(entered_choice, account, store_details)
            elif entered_choice == 8:
                store_details = fetch_info(entered_choice, account, store_details)
                # if len(store_details) == 0:
                #     os.system("cls" if os.name == "nt" else "clear")
                #     bank_account_main()()
                #     break
            elif entered_choice == 9:
                break
            else:
                console.print(
                    "You must enter 1,2,3,4,5,6,7 or 8", style="bold red on black"
                )

    return run_bank_account


if __name__ == "__main__":
    end_loop = True
    console = Console()
    try:
        # user_data = (
        #     read_data("user-list") if type(read_data("user-list")) is dict else {}
        # )
        all_data = (
            read_data("user-list") if type(read_data("user-list")) is dict else {}
        )

        for item in all_data.values():
            if item.get("type") == "Savings":
                account = SavingsAccount(item.get("name"), float(item.get("balance")))
            else:
                account = CurrentAccount(item.get("name"), float(item.get("balance")))
            types = 1 if account.type == "Savings" else 2
            user_data[item.get("name") + str(types)] = account
            # print("user_data=", user_data)
        os.system("cls" if os.name == "nt" else "clear")
        exec_bank_account = bank_account_main()
        exec_bank_account()
    except Exception as error:
        console.print(f"\nError occurred at: \n{error}\n", style="bold red on black")
        sys.exit()
