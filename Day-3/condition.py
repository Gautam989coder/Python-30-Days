# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 33
b = 200
if b > a:
  print("b is greater than a")


# =======================================================================================================
# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

# Multiple statements in an if block:

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")  




# Boolean variables can be used directly in if statements without comparison operators.
# Using a boolean variable:

is_logged_in = True
if is_logged_in:
  print("Welcome back!")  


# The Elif Keyword
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#  Multiple Elif Statements
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D") 



# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition
# Day of the week checker:

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")




# The Else Keyword
# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")  



# You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")  


# You can combine if, elif, and else to create a comprehensive decision-making structure
# Temperature classifier:

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")  




# Python Shorthand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
# One-line if statement:

a = 5
b = 2
if a > b: print("a is greater than b")



# Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a :
  print("a is greater than both b and c")
  print("Both conditions are True")




# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")  




# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")  



# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass



