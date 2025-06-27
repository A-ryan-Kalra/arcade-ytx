class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, name, initialAmount):
        self.name = name
        self.balance = initialAmount
        print(f"\nAccount {self.name} created\nBalance = ${self.balance:,.2f}\n")

    def show_balance(self):
        print(f"\nCurrent balance : ${self.balance:,.2f}\n")

    def deposit(self, amount):
        self.balance += amount

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                "\nSorry, not enough balance to continue with the transaction.\n"
            )

    def withdraw_amount(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw Completed...")
            self.show_balance()
        except BalanceException as error:
            print(error)

    def transfer_amount(self, amount, account):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            account.deposit(amount)
            print("\nTransfer Completed...")
            self.show_balance()
            # account.show_balance()
        except BalanceException as error:
            print(error)


class InterestRewardAccount(BankAccount):

    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit Completed...")
        self.show_balance()


class SavingsAccount(InterestRewardAccount):
    def __init__(self, name, initialAmount):
        self.fee = 5
        super().__init__(name, initialAmount)

    def withdraw_amount(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw Completed...")
            self.show_balance()
        except BalanceException as error:
            print(error)


if __name__ == "__main__":
    aryan = BankAccount("Aryan Kalra", 1221)
    shubham = SavingsAccount("Shubham Kalra", 300)
    aryan.show_balance()
    # aryan.deposit(2000)
    shubham.deposit(2000)
    # aryan.show_balance()
    shubham.withdraw_amount(2000)
    # aryan.transfer_amount(200, shubham)
    # aryan.withdraw_amount(2341)
