data = {
        123456:{"pin":7890,"Balance":10000,"History":[]},
        234567:{"pin":8901,"Balance":8000,"History":[]},
        345678:{"pin":9012,"Balnace":5000,"History":[]},
        }

print("Welcome To ATM")
acc = int(input("Enter account number: "))
pin=int(input("Enter PIN Number: "))
if acc in data and data[acc]["pin"] == pin:
    print("Login Successfull.\n")

    while True:
        print('''ATM MENU
        1.Check Balance
        2.Deposit
        3.Withdraw
        4.View Transactions
        5.Exit''')

        op=int(input("Select Option: "))
        
        if op ==1:
            print(f"Current Balance: ₹ {data[acc]['Balance']}\n")

        elif op ==2:
            amount = int(input("Enter amount to deposit: "))
            data[acc]["Balance"]+=amount
            data[acc]["History"].append(f"Deposited ₹{amount}")
            print(f"Successfully deposited amount ₹ {amount}\n")

        elif op == 3:
            amount = int(input("Enter amount to Withdraw: "))
            if data[acc]["Balance"]>=amount:
               data[acc]["Balance"]-=amount
               print(f"Successfully Withdrawn amount ₹ {amount}\n")
            else:
                print("Unsufficient Balance")
            data[acc]["History"].append(f"Withdrawn ₹{amount}\n")

        elif op == 4:
            print("Transaction History: ")
            for i in data[acc]["History"]:
                print(f"- {i}")

        elif op == 5:
            break
        else:
            print("Invalid Option")
              
             
else:
    print("Invalid account number or PIN")