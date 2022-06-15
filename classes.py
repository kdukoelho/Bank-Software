from random import randint


class Account:
    a_number = ''.join((str(randint(1, 9)), str(randint(1, 9)), str(randint(1, 9))))
    a_number = str(a_number)

    def __init__(self, name, balance=0, limit=5000):
        self.name = name
        self.balance = balance
        self.limit = limit

    def account_statement(self):
        print(f'Name: {self.name} \n'
              f'Account number: {self.a_number} \n'
              f'Balance: {self.balance}')

    def withdraw(self, withdraw_value):
        self.balance -= withdraw_value
        print(f'Withdraw value: {withdraw_value} \n'
              f'Current balance: {self.balance}')

    def deposit(self, deposit_value):
        self.balance += deposit_value
        print(f'Deposit value: {deposit_value} \n'
              f'Current balance: {self.balance}')
