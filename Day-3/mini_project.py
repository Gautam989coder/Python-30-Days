# Simple Bank Account System
# ========= Bank Acount ===============



balance = 10000

while(True):
    print("Bank Account")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    option = int(input("Plz Enter your Option: "))
    if option == 1 :
        print("your balance is:", balance)
    elif option == 2 :
        deposit = int(input("Enter deposite amount: "))
        if deposit <= 0:
           print("Invalid deposit amount") 
        else:
           balance = balance + deposit
           print(f"₹{deposit} Deposite.") 
           print(f"New Balance: {balance}")  
    elif option == 3: 
        withdrawl = int(input("Enter Withdrawl Amount: "))
        if withdrawl <= 0:
            print("Invalid withdrawal amount")
        elif withdrawl > balance:
            print("Insufficient balance")
        else :
            balance = balance - withdrawl
            print(f'₹{withdrawl} withdrawl Successfull') 
            print(f'Remianing Balance: {balance}')
           
    elif option == 4 :
        print("Thank you for using our bank.")
        break        
    else:
        print("Invalid choice.")

