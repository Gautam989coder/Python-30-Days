# Create four functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).
# Each function should return its result. Ask the user for two numbers and display the results.
# Extra requirement: Do not divide by zero. Display a helpful message instead.  


def add(a, b):
    return a + b

a1 = add(4, 4)
print(a1)
a2 = add(9, 2)
print(a2)


def subtract(a, b):
    return a - b 

b1 = subtract(8, 6)
print(b1)
b2 = subtract(6, 9)
print(b2)



def multiply(x, y):
    return x * y

x1 = multiply(6, 6)
print(x1)
x2 = multiply(4, 5)
print(x2)



def divide(x, y):
    if y == 0:
        # print("Do not divide by zero")
        return "Do not divide by zero"
    # else:
    #     print(f'{x} is devisible by {y}')
    return x / y    
    
d1 = divide(10, 0)
print(d1) 
d2 = divide(8, 3)
print(d2)       
