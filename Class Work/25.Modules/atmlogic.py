data={
    '1234':{'balance':45678,'pin':123,'history':[]},
    '5678':{'balance':56789,'pin':123,'history':[]},
    '5690':{'balance':98798,'pin':123,'history':[]},
    '5612':{'balance':45678,'pin':123,'history':[]},
    '2345':{'balance':45678,'pin':123,'history':[]},
    '6789':{'balance':45678,'pin':123,'history':[]},
    }
acc_num=None
login_status=False

def welcome():
    print("Welcome to ATM".center(40,'-'))

def menu():
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.View Transaction')
    print('0.Exit')
    
def login(acc,pin):
    if acc in data:
        if data[acc]['pin']==pin:
            global acc_num
            global login_status
            acc_num=acc
            login_status=True
            print("Login Successful")
        else:
            print("Invalid login")
    else:
        print("Invalid Account number")

def check_balance():
    if login_status and acc_num:
        print(f"Current Balance: {data[acc_num]['balance']}")
    else:
        print("Login Again")

def deposit():
    if login_status and acc_num:
        amount=int(input("Enter the amount to deposit: "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited: ${amount}')
        print(f'{amount} is successfully deposited')
    else:
        print("Login Again")

def withdraw():
    if login_status and acc_num:
        amount=int(input("Enter the amount to withdraw: "))
        if amount<=data[acc_num]['balance']:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdrawn: ${amount}')
            print(f'{amount} is successfully Withdrawn')
        else:
            print("Insufficient Balance")
    else:
        print("Login Again")

def view_transaction():
    if login_status and acc_num:
        if data[acc_num]['history']:
            print("\nTransactions: ")
            for i in data[acc_num]['history']:
                print(i)
            print("End of the transaction\n")
        else:
            print("No Transactions")
    else:
        print("Login Again")
    

    
