class Account:
    accounts = []
    BalanceOfBank = 0
    LoanFromBank = 0

    def __init__(self,name,email,adress,accountType):
        self.name = name
        self.email = email
        self.address = address
        self.accountType = accountType
        self.balance = 0
        self.transactionHistory = []
        self.accountNumber = len(Account.accounts)+20001
        Account.accounts.append(self)
        self.numOfLoans = 0

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            Account.BalanceOfBank += amount
            print(f'\n You have successfully deposited the amount of {amount} Taka.')
            print(f'\n Your current balance is: {self.balance} Taka.')
        else:
            print('Please deposit a positive amount of taka')
    def withdraw(self,amount):
        if(amount>=0 and amount<=self.balance):
            self.balance -= amount
            Account.BalanceOfBank -= amount
            print(f'\n You have successfully withdrawn the amount of {amount} Taka.')
            print(f'\n Your current balance is: {self.balance} Taka.')
            self.transactionHistory.append(f'Successfully withdrawn {amount} taka')

    def check_available_balance(self):
        print(f'\nYour current balance is: {self.balance}')

    def transaction_history(self):
        print('\n__________________ Transition History ____________________')
        for history in self.transactionHistory:
            print(history)

    def take_loan(self,amount):
        if self.numOfLoans <3:
            if amount > 0:
                self.balance += amount
                self.numOfLoans += 1
                Account.BalanceOfBank -= amount
                Account.LoanFromBank += amount
                print(f'\n{amount} tk loan is successfully taken from bank\n')
                self.transactionHistory.append(f'\nLoan taken: {amount} Taka\n')
            else:
                print("\nInvalid amount.")

        else:
            print('You have already taken the maximum amount of permitted loan')

    def transfer_money(self,acnt_num,amount):
        flag = False
        for num in self.accounts:
            if num.accountNumber == acnt_num:
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    person.balance += amount
                    flag = True
                    print(f'\n {amount} taka transfarred succesfully\n')
                    self.transition_history.append(f'\nSuccessfully transfarred: {amount} taka\n')

                else:
                    flag = True
                    print('\nInvalid amount.\n')

        if flag == False:
            print('\nAccount does not exist of this number\n')

    def __repr__(self) -> str:
        print(f'User Name: {self.name}')
        print(f'User Adress: {self.adress}')
        print(f'account type: {self.accountType}')
        print(f'Balance: {self.balance}')
        print(f'Email: {self.email}')
        print(f'account number is: {self.accountNumber}')
        return ''

class Admin(Account):
    bank_admin = []
    def __init__(self,name,adminID,password) -> None:
        self.name = name
        self.adminID = adminID
        self.password = password
        self.adminAccounts = []
        self.loan_approval = True
        Admin.bank_admin.append(self)

    def delete_account(self,accntNum):
        flag = False
        for accnt in admin.adminAccounts:
            if accnt.accountNumber == accntNum:
                flag = True
                Account.BalanceOfBank -= accnt.balance
                admin.adminAccounts.remove(accnt)
                Account.accounts.remove(accnt)
        if flag == True:
            print('\nAccount deleted Successfully.\n')
        else:
            print('This account does not exist.')


admin = None
user = None

while True:
    print('1. Admin')
    print('2. User')
    print('3. Exit')

    op = int(input('Choose your option: '))

    if op == 1:
        while True:
            if admin == None:
                print('________ Welcome Sir/Madam _________')
                ch = input('Register/Login (R/L) : ')
                if ch == 'R':
                    print('Admin info:')
                    print('Nmae: admin, Id: admin , Password: admin@#@34')
                    name = input("Enter your name: ")
                    id1 = input("Enter your id: ")
                    password = input("Enter your Password: ")
                    admin = Admin(name, id1, password)
                elif ch == 'L':
                    print('Admin info:')
                    print('Nmae: admin, Id: admin , Password: admin@#@34')
                    name2 = input("Enter your name: ")
                    id2 = input("Enter your id: ")
                    password2 = input("Enter your Password: ")

                    for admin2 in Admin.bank_admin:
                        if admin2.name == name2 and admin2.adminID == id2 and admin2.password == password2:
                            admin = admin2
            else:
                    print('_____WELCOME TO OUR BANKING SYSTEM_____')
                    print('Please choose your option: ')
                    print("1. Create an user account")
                    print("2. Delete an user account")
                    print("3. See all users accounts list")
                    print("4. Check the total available balance of the bank")
                    print("5. Check the total loan amount")
                    print("6. Exit")


                    opt = int(input('Choose option:'))

                    if opt == 1:
                        name = input('Name: ')
                        email = input('Email: ')
                        address = input('Adress: ')
                        accntType = input('Account type: ')

                        account1 = Account(name,email,address,accntType)
                        admin.adminAccounts.append(account1)
                        print('Account is Created Successfully.')

                    elif opt == 2:
                        acnt_num = int(input('give account number:'))
                        admin.delete_account(acnt_num)
                    elif opt == 3:
                        print('\n_________ All account in our list _________')
                        for accntMan in admin.adminAccounts:
                            print(accntMan)
                    elif opt == 4:
                        print(f'Total available balance of bank: {admin.BalanceOfBank}')
                    elif opt == 5:
                        print(f'Total loan of bank: {admin.LoanFromBank}')
                    elif opt == 6:
                        admin = None
                        break
    elif op == 2:
        while True:
            if user == None:
                print('\n________Give your information for login_________\n')
                name=input('User name:')
                email=input('User email:')
                address=input('User address:')
                acntType=input('User account type:')
                flag = False

                for user1 in Account.accounts:
                    if user1.name == name and user1.email == email and user1.address == address:
                        user = user1
                        flag = True

                if flag == False:
                    print('There is no account.')
            else:
                print('\n__________Welcome User___________')
                print('1. Deposit money in your account')
                print('2. Withdraw money from your account')
                print('3. Your available Balance')
                print('4. All transaction')
                print('5. Take loan from bank')
                print('6. Transfer money to another account')
                print('7. Exit')

                ch1 = int(input('Choose option:'))

                if ch1 == 1:
                    amnt = int(input('Deposit amount: '))
                    user.deposit(amnt)
                elif ch1 == 2:
                    amnt = int(input('Withdraw amount: '))
                    user.withdraw(amnt)
                elif ch1 == 3:
                    user.check_available_balance()

                elif ch1 == 4:
                    user.transaction_history()
                elif ch1 == 5:
                    amnt = int(input('Loan amount: '))
                    if amnt <= Account.BalanceOfBank:
                        user.take_loan(amnt)
                    else:
                        print('Sorry Sir/Madam, Our bank does not have enough money!!')

                elif ch1 == 6:
                    frnd = int(input('Give transfer account number: '))
                    amnt = int(input('Give the amount you want to transfer: '))
                    user.transfer_money(frnd,amnt)
                elif ch1==7:
                    user=None
                    break
    elif op == 3:
        print('______ Thanks for using our bank _______')
        break





