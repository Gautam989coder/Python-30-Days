# In Python, a function is a reusable block of code designed to perform a specific task.
# Functions help break down large programs into smaller, organized, and manageable pieces.
# They only execute when they are explicitly called


# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
  print("Hello from a function")


# Calling a Function
# def my_function():
#   print("Hello from a function")

my_function()


# Function Names
# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)


#===================================================================================
# Python Function Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_function(fname): # here fname is parameter 
  print(fname + " Refsnes")

my_function("Emil")  # emil is argument
my_function("Tobias") # Tobis is argument
my_function("Linus")   #Linus is agrument



# Multiple parameters
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# If you try to call the function with the wrong number of arguments, you will get an error:



# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function()
my_function("Tobias")


