from classes import Account

accounts_list = list()
operation_choice = int(input('1 - Access account \n'
                             '2 - Create account \n'
                             'Your choice: '))
if operation_choice == 1:
    user_name = str(input('Name: '))
    user_a_number = str(input('Account number: '))
    user_choice = int(input('1 - Account Statement \n'
                            '2 - Withdraw \n'
                            '3 - Deposit \n'
                            'Your choice: '))

elif operation_choice == 2:
    user_name = str(input('Name: ')).capitalize()
    deposit_value = int(input('!!If you dont want to deposit now, press 0!!\n'
                              'Amount to be deposited: '))
    account = Account(user_name, deposit_value)
    accounts_list.append(account)
    print(f'---Account created.---')
    account.account_statement()
    print(f'---Account created.---')
