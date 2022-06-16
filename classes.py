from random import randint


class Account:

    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance
        self.a_number = None

    def generate_a_number(self):
        self.a_number = ''.join((str(randint(1, 9)), str(randint(1, 9)), str(randint(1, 9))))
        self.a_number = str(self.a_number)

    def account_statement(self):
        print(f'Name: {self.name} \n'
              f'Account number: {self.a_number} \n'
              f'Balance: {self.balance}')

    def withdraw(self, withdraw_value):
        self.balance -= withdraw_value

    def deposit(self, deposit_value):
        self.balance += deposit_value
