# Variables
# Variables are containers for storing data values.

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# legal variable names
myvar = "John"
my_var = "tom"
_my_var = "Ram"
myVar = "Jonny"
MYVAR = "Jack"
myvar2 = "samm"

# illegal variable names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"


# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"



# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
g = 5
h = "John"
print(g + h)


# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)