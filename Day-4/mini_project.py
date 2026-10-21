# Bank Account System — Version 2
# I already started a basic bank account program on Day 3. Today, I will upgrade that program using loops.

# Requirements
# 1. Check Balance: Display the current balance.
# 2. Deposit Money: Ask for an amount and add it to the balance. Reject zero or negative amounts.
# 3. Withdraw Money: Check that the amount is positive and does not exceed the balance.
# 4. Exit: Display a goodbye message and stop the program.
# 5. Invalid choice: Display an error message and show the menu again.



balance = 10000

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice ==  1:
        print(f'Balance: {balance}')
    elif choice == 2:
        deposite = int(input("Enter deposite amount: "))
        if deposite <= 0:
            print("Invalid Amount")
        else:
            balance += deposite  
            print(f'{deposite} deposit')
    elif choice == 3:
        withdrawl = int(input("Enter withdrawl amount: "))
        if withdrawl > balance:
            print("Insufficient balance")
        elif withdrawl <= 0:
            print("Invalid withdrawal amount") 
        else:
            balance -= withdrawl
            print(f'₹{withdrawl} withdrawl Successfull') 
            print(f'Remianing Balance: {balance}') 
    elif choice == 4:
        print("Thank you for using our bank.")
        break  
                      
    else:
        print("invalid choice")        