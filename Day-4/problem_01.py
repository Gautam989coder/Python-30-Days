# Ask the user for a number and print its multiplication table from 1 to 10.
# Example: if the input is 5, print 5 x 1 = 5 through 5 x 10 = 50.
# Concepts: input(), int(), for, range()

num = int(input("Enter Number: "))

for i in range(1, 11):
    print(f'{num} X {i} = {num*i}')