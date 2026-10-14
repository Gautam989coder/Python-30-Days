# ATM withdrow


Balance =  1000
amount = int(input("Enter Amount: "))

 
if amount <= 0:
    print("invalid amount")
elif amount > Balance:
    print("Insafficint balance")
else:
    Balance -=  amount
    print("Withdrawl successfull")
    print(f'Remaining balance {Balance}')

