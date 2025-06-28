class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, name, initialAmount, type="Savings"):
        self.name = name
        self.balance = initialAmount
        self.type = type
        print(
            f"\nAccount '{self.name}' created.\tType = '{self.type}'\nBalance = ${self.balance:,.2f}.\nPlease note, a 5% interest has been applied 🎉.\n"
        )

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

    def viable_transaction_current(self, amount, overdraft_limit):
        if amount > self.balance:
            if amount - self.balance <= overdraft_limit:
                self.balance -= amount
                print("\nWithdraw Completed...")
                self.show_balance()
            else:
                raise BalanceException("\nInsufficient funds\n")
        else:
            self.balance -= amount
            print("\nWithdraw Completed...")

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
        except BalanceException as error:
            print(error)


class InterestRewardAccount(BankAccount):

    def deposit(self, amount):
        self.balance += amount * 1.05
        print(
            "\nDeposit Completed...\nPlease note, a 5% interest will be applied on each deposit 🎉\n"
        )
        self.show_balance()


class SavingsAccount(InterestRewardAccount):
    def __init__(self, name, initialAmount):
        self.fee = 1.01
        super().__init__(name, initialAmount * 1.05, type="Savings")

    def withdraw_amount(self, amount):
        try:
            self.viable_transaction(amount * self.fee)
            self.balance -= amount * self.fee
            print(
                "\nWithdraw Completed...\nPlease note, a 1% interest fee has been charged\n"
            )
            self.show_balance()
        except BalanceException as error:
            print(error)


class CurrentAccount(BankAccount):
    def __init__(self, name, initialAmount):
        self.overdraft_limit = 1000
        super().__init__(name, initialAmount, type="Current")

    def withdraw_amount(self, amount):
        try:
            self.viable_transaction_current(amount, self.overdraft_limit)
        except BalanceException as error:
            print(error)
