# Expense Tracker
# Ask the user to enter daily expenses one at a time. Entering 0 should stop input. Then display the total expenses and the number of expenses entered.
# Example: 100, 50, 200, 0 → total 350, count 3.
# Concepts: while, conditions, counters, accumulators




# total = 0 
# count = 0 
# while True:
#     expense = int(input("Enter your daily expense: "))
#     if expense == 0:
#         break
#     elif expense < 0:
#         print("Invalid expense")
#         continue
#     total = total + expense
#     count += 1
# print(f"Total expenses: ₹{total}")
# print(f"Number of expenses: {count}")





total = [ ]  # Here i use a list 
count = 0 
while True:
    expense = int(input("Enter your daily expense: "))
    if expense == 0:
       break
    elif expense < 0:
       print("Invalid expense")
       continue
    total.append(expense)
    count += 1
print(f'Here your expenses list {total}')
total_expense = sum(total)
print(f"Total expenses: ₹{total_expense}")
print(f"Number of expenses: {count}")
