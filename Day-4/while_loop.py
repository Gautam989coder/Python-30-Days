# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i], end="")
    i += 1  
#================================================== 


# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")    




# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")    





# for	When you want to repeat something over a sequence or a known range
# while	When you want to repeat something while a condition remains true  