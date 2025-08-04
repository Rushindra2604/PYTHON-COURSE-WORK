data={"balance":5000,"history":[]}

def current_balance():
    print(f"Current Balance - {data['balance']}.\n")

def deposit():
    amount=int(input("Enter the amount: "))
    data['balance']+=amount
    data['history'].append(f"deposited-{amount}.")
    print(f"deposited-{amount}.\n")

def withdraw():
    amount=int(input("Enter the amount: "))
    if amount<=data['balance']:
        data['balance']-=amount
        data['history'].append(f"withdraw-{amount}.")
        print(f"withdraw-{amount}.\n")
    else:
        print("Insufficient balance.\n")

def history():
    if history:
        for i in data['history']:
            print(i)
        print()
    else:
        print("No transaction.")

while True:
    print("Welcome to ATM")
    print('1. Current Balance')
    print('2. Deposit')
    print('3. withdraw')
    print('4. history')
    print('0. Exit')
    ch=int(input("Enter Your Choice: "))

    if ch==1:
        current_balance()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        history()
    elif ch==0:
        break
    else:
        print("Invalid.\n")