import sys
import start_program
import accountClass
import depositMoney
import withdrawMoney

user_action = start_program.option_chosen()
while user_action != 'Exit':

    if user_action == 'Get Account Info':
        accountClass.obj_account.getAccountInfo()

    elif user_action == 'Deposit Money':
        print('Enter amount to deposit:')
        amount = input()
        print('Type "Y" if you want to continue or "N" to cancel:')
        transaction_resolution = input()
        depositMoney.deposit(amount, transaction_resolution)

    elif user_action == 'Withdraw Money':
        print('Enter amount to withdraw:')
        withdraw_amount = input()
        withdrawMoney.withdraw(withdraw_amount)

    else:
        accountClass.obj_account.get_balance()

    print('Continue or exit program: ')
    user_action = start_program.option_chosen()
    
print('Exit')
sys.exit()