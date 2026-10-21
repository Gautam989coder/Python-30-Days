# Ask the user for a positive number n. Calculate the sum of all numbers from 1 to n using a loop.
# Example: input 5 → output 15, because 1 + 2 + 3 + 4 + 5 = 15.
# Concepts: for, range(), variables


n = int(input("Enter a positive number: "))
total = 0 

if n <= 0:
    print("Maybe You enter 0 or -ve number")
else:    
    for i in range(1, n + 1):
        total = total + i

    print(f"Sum: {total}") 
   
