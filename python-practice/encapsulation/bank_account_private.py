class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance =", self.__balance)

acc = BankAccount(1000)

acc.deposit(500)
acc.show_balance()