# Python For Loops
# Python for loops are used to iterate over sequences such as lists, tuples, strings and ranges.
# Allows the same operation to be applied to every item in a sequence.


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# range() Method
# range() function is used with for loops to generate a sequence of numbers. It can take one, two or three arguments:
# range(stop) generates numbers from 0 to stop-1.
# range(start, stop) generates numbers from start to stop-1.
# range(start, stop, step) generates numbers from start to stop-1, incrementing by step.

for i in range(4):
    print(i)  

for i in range(0, 10):
    print(i) 

for i in range(0, 10, 2):
    print(i)     


# Loop through the letters in the word "banana":

for x in "banana":
  print(x)      




# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break  


# for i in 'geeksforgeeks':
#     if i == 'e' or i == 's':
#         break
#     print(i)  



# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)    


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")  



# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")  




# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":  

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass    



# Using Enumerate
# enumerate() is used with a for loop to access both the index and the value of each item during iteration.

b = ["eat", "sleep", "repeat"]
for i, j in enumerate(b):
    print (i, j)

# Explanation:
# enumerate(b) returns both index and value from list b.
# i stores index values and j stores list items.   


for i in range(1, 10):
  print(f'{i} square is {i*i}')