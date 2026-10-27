#Expense Summary
# Create separate functions to calculate:
# - Total expenses
# - Average expense
# - Highest expense
# Each function should return a value. Print the results after calling the functions.


def total_expense(expense):
    total = sum(expense)
    return total

def average_expense(expense):
    average = sum(expense) / len(expense)
    return average  

def highest_expense(expense):
    highest = max(expense)
    return highest 
'''
for max value calculate 
high = expense[0]
   for i in expense:
      if i > high:
         high = i
'''         


expense = [2, 25, 7, 9, 17, 5]  
s1 = total_expense(expense)  
print(s1)

s2 = average_expense(expense)
print(s2)

s3 = highest_expense(expense)
print(s3)




def expense_summary(expense):
    total = sum(expense)
    average = sum(expense) // len(expense)
    highest = max(expense)

    return total, average, highest

expense = [2, 24, 5, 3, 16, 9, 7] 
total, average, highest = expense_summary(expense)

print(f'Total expense: {total}')
print(f'Average expense: {average}')
print(f'Highest expense: {highest}')