from bankClass import bank

class account(bank):
    def __init__(self, IFSC_Code, bankname, branchname, loc, AccountID, Customer, balance):
        super().__init__(IFSC_Code, bankname, branchname, loc)
        self.AccountID = AccountID
        self.Customer = Customer
        self.balance = balance

    def getAccountInfo(self):
        print('Account Info:')
        print('\t IFSC Code:', self.IFSC_Code)
        print('\t Bank Name:', self.bankname)
        print('\t Branch Name:', self.branchname)
        print('\t Bank Location:', self.location)
        print('\t Account Id:', self.AccountID)
        print('\t Customer:', self.Customer)
        print('\t Account balance: $', self.balance, sep='')

    def deposit(self, amount, accepted):
        type = 'accepted' if accepted == 'Y' else "N"
        print('Deposit ' + type + ':')
        print('\t Account Id:', self.AccountID)
        print('\t Deposit Amount: $', amount, sep='')
        if accepted == 'Y':
            print('\t Previous Account balance: $', self.balance, sep='')
            self.balance = int(amount) + int(self.balance)
            print('\t New Account balance: $', self.balance, sep='')
        else:
            print('\t Deposit is not accepted. Account balance: $', self.balance, sep='')

    def withdraw(self, amount):
        print('Withdraw:')
        if self.balance < int(amount):
            print('\t You cannot withdraw {} USD. Your current balance is {}'.format(amount, self.balance))
        else:
            print('\t Account Id:', self.AccountID)
            print('\t Withdraw Amount: $', amount, sep='')
            self.balance = int(self.balance) - int(amount)
            print('\t New Account balance: $', self.balance, sep='')

    def get_balance(self):
        print('Your Current Balance:')
        print('\t Balance: $', self.balance, sep='')

obj_account = account("SBIN0005943", "Chase", "5943" , "Santa Barbara", "56393475", "Mikel Rodriguez", 500)