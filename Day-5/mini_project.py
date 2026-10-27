#Mini-project: Expense Tracker
# Now I will build something useful by combining functions with lists, loops, and conditions.

# What the program should do
# Display a menu:
# ===== EXPENSE TRACKER =====

# 1. Add Expense
# 2. View All Expenses
# 3. View Total Expenses
# 4. Exit
# Start with an empty list:
# expenses = []
# Implement these features:
# 1. Add Expense: Ask for an expense description and amount. Store both together in a dictionary and add it to the list.
# 2. View All Expenses: Display every expense with its description and amount. If the list is empty, display a message.
# 3. View Total Expenses: Calculate and display the total amount spent.
# 4. Exit: Stop the program.
# For example, an expense could be stored like this:
# expense = {    "description": "Lunch",    "amount": 120}
# I can add this dictionary to the expenses list.
# Your main challenge
# Create separate functions such as:
# - add_expense()
# - view_expenses()
# - calculate_total()
# - main()
# Use a while loop inside main() to keep the menu running.




expenses = []

def add_expense():
    discription = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "discription": discription,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

# add_expense()
# add_expense()


def view_expenses():
    if not expenses:
        print("No expenses found")
    else:
        for i in expenses:
            print(f'Description: {i["discription"]}')
            print(f'Amount: {i["amount"]}') 

# view_expenses()


def calculate_total():
    total = 0 
    for i in expenses:
        total = total + i["amount"]
    return total

# d4 = calculate_total()
# print(d4)

def main():
    while(True):
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_expense()
        elif choice ==  "2":
            view_expenses()
        elif choice == "3":
            print(f'Total Expense: {calculate_total()}')
        elif choice == "4":
            print("Goodbye")
            break 
        else:
             print("Invalid choice. Try again.")   
    
# main()  

if __name__ == "__main__":
    main()



