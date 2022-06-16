from classes import Account

accounts_list = list()
a_number_list = list()
while True:
    print('=' * 20)
    operation_choice = int(input('1 - Access account \n'
                                 '2 - Create account \n'
                                 '3 - Close \n'
                                 '====================\n'
                                 'Your choice: '))

    print('=' * 20)
    if operation_choice == 1:  # Login #
        user_name = str(input('Name: ')).lstrip().capitalize()
        user_password = str(input('Password: '))
        user_a_number = str(input('Account number: '))

        for account in accounts_list:
            if account.name == user_name and account.password == user_password and account.a_number == user_a_number:
                while True:
                    print('=' * 20)
                    user_choice = int(input('1 - Account Statement \n'
                                            '2 - Withdraw \n'
                                            '3 - Deposit \n'
                                            '4 - Close \n'
                                            '====================\n'
                                            'Your choice: '))
                    if user_choice == 1:
                        print('=' * 20)
                        print('\n==Account Statement==')
                        account.account_statement()
                        print('==Account Statement==\n')
                    elif user_choice == 2:
                        print('=' * 20)
                        withdraw_value = float(input(print(f'Current balance {account.balance}\n'
                                                           f'Withdraw value: ')))
                        if account.balance < withdraw_value:
                            print('=' * 20)
                            print(f'You dont have enough money\n'
                                  f'Your balance: {account.balance}')
                        else:
                            account.withdraw(withdraw_value)
                            print('=' * 20)
                            print(f'\n---Withdraw success---\n'
                                  f'Current balance: ${account.balance}\n'
                                  f'Withdraw value: ${withdraw_value}\n'
                                  f'---Withdraw success---\n')
                    elif user_choice == 3:
                        print('=' * 20)
                        deposit_value = float(input(f'Current balance: {account.balance}\n'
                                                    'Deposit value: $'))
                        print('=' * 20)
                        account.deposit(deposit_value)
                        print(f'\n---Deposit success---\n'
                              f'Current balance ${account.balance}\n'
                              f'Deposit value: ${deposit_value}\n'
                              f'---Deposit success---\n')
                    elif user_choice == 4:
                        break
                    else:
                        print('\nPlease select a valid value.\n')
                        continue
            else:
                print(f'\nAccount "{user_name} | {user_a_number}" no exist.\n')

    elif operation_choice == 2:  # Creating an account #
        user_name = str(input('Name: ')).capitalize().lstrip()
        user_password = str(input('Password: '))

        deposit_value = int(input('---If you dont want to deposit now, press 0---\n'
                                  'Amount to be deposited: '))
        print('=' * 20)
        account = Account(user_name, user_password, deposit_value)
        account.generate_a_number()

        if account.a_number in a_number_list:  # If account number already exist create a new account number #
            while account.a_number in a_number_list:
                account.generate_a_number()

        accounts_list.append(account)
        a_number_list.append(account.a_number)
        print(f'!!!Please, save that data.!!!')
        print(f'\n==Account created==')
        account.account_statement()
        print(f'==Account created==\n')
    elif operation_choice == 3:
        print('Closing software...')
        break

    else:
        print('\nPlease select a valid value.\n')
        continue
