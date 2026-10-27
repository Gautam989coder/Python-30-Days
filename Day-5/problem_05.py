# aTM Operations
# Create three functions:
# - check_balance(balance) — returns the balance.
# - deposit(balance, amount) — returns the updated balance if the amount is positive.
# - withdraw(balance, amount) — returns the updated balance if the amount is valid and sufficient.
# Start with a balance of ₹10,000. Test deposits and withdrawals by calling the functions.

# If an operation is invalid, show a suitable message and keep the balance unchanged.



def check_balance(balance):
    return balance

def deposit(balance, amount):
    if amount <= 0 :
        print("Invalid amount. Deposit must be positive.")
        return balance
    balance = balance + amount
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        print("Invalid amount. Withdrawal must be positive.")
        return balance
        
    elif amount > balance:
        print("Insufficient balance")
        return balance
    else:
        balance = balance - amount
        return balance 

    
balance = 10000
print(f'Starting Balance: {check_balance(balance)}')
print("===========================================================")

balance = deposit(balance, 1000)
print("Balance after deposit:", check_balance(balance))
print("===========================================================")

balance = withdraw(balance, 8000)
print("Balance after withdraw", check_balance(balance))
print("===========================================================")

balance = deposit(balance, 0)
print("Final balance:", check_balance(balance))