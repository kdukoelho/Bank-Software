from classes import Account


accounts_list = list()
a_number_list = list()

while True:
    print('=' * 20)
    operation_choice = input('1 - Access account \n'
                             '2 - Create account \n'
                             '3 - Close \n'
                             '====================\n'
                             'Your choice: ')

    print('=' * 20)

    while operation_choice.isalpha():
        operation_choice = input('Please insert only numbers.\n'
                                 'Your choice: ')
        print('=' * 20)
    operation_choice = int(operation_choice)

    if operation_choice == 1:  # Login #
        user_name = str(input('Name: ')).upper().lstrip()
        user_password = str(input('Password: '))
        user_a_number = str(input('Account number: '))

        for account in accounts_list:
            if account.name == user_name and account.password == user_password and account.a_number == user_a_number:
                while True:
                    print('=' * 20)
                    user_choice = input('1 - Account Statement \n'
                                        '2 - Withdraw \n'
                                        '3 - Deposit \n'
                                        '4 - Close \n'
                                        '====================\n'
                                        'Your choice: ')

                    while user_choice.isalpha():
                        user_choice = input('Please insert only numbers\n'
                                            'Your choice: ')
                        print('=' * 20)
                    user_choice = int(user_choice)

                    if user_choice == 1:
                        print('=' * 20)
                        print('\n==Account Statement==')
                        account.account_statement()
                        print('==Account Statement==\n')

                    elif user_choice == 2:
                        print('=' * 20)
                        withdraw_value = input(f'Current balance {account.balance}\n'
                                               f'Withdraw value: $')

                        while withdraw_value.isalpha():
                            withdraw_value = input('Please insert only numbers.\n'
                                                   'Withdraw value: ')
                        withdraw_value = float(withdraw_value)

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
                        deposit_value = input(f'Current balance: {account.balance}\n'
                                              'Deposit value: $')

                        while deposit_value.isalpha():
                            deposit_value = input('Please insert only numbers.\n'
                                                  'Deposit value: ')
                        deposit_value = float(deposit_value)

                        account.deposit(deposit_value)
                        print('=' * 20)
                        print(f'\n---Deposit success---\n'
                              f'Current balance ${account.balance}\n'
                              f'Deposit value: ${deposit_value}\n'
                              f'---Deposit success---\n')
                    elif user_choice == 4:
                        break
                    else:
                        print('=' * 20)
                        print('\nPlease select a value between 1 and 4.\n')
                        continue
            elif user_name == account.name and user_a_number == account.a_number and user_password != account.password:
                print(f'\nWrong password.\n')

            else:
                print(f'\nAccount "{user_name} | {user_a_number}" no exist.\n')

    elif operation_choice == 2:  # Creating an account #
        user_name = input('Account owner fullname: ').upper().lstrip()
        user_password = str(input('Create password: '))

        while len(user_password) < 8:
            user_password = input('Password needs at least 8 chars.\n'
                                  'Create password: ')

        deposit_value = input('---If you dont want to deposit now, press 0---\n'
                              'Amount to be deposited: ')

        while deposit_value.isalpha():
            deposit_value = input('Please insert only numbers.\n'
                                  'Amount to be deposited: ')
        deposit_value = float(deposit_value)

        while deposit_value <= float(-1):
            deposit_value = 'Please insert a value greater than -1\n' \
                            'Amount to be deposited: '

        print('=' * 20)

        account = Account(user_name, user_password, deposit_value)
        account.generate_a_number()

        if account.a_number in a_number_list:  # If account number already exist create a new account number #
            while account.a_number in a_number_list:
                account.generate_a_number()

        accounts_list.append(account)
        a_number_list.append(account.a_number)

        print(f'!!!Please, save that data!!!')
        print(f'\n==Account created==')
        account.account_statement()
        print(f'==Account created==\n')

    elif operation_choice == 3:
        print('Exiting...')
        break

    else:
        print('\nPlease select a value between 1 and 3.\n')
        continue
