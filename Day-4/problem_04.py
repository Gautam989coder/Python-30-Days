# Login Attempts
# Set the correct username to "admin" and password to "12345".
# Allow a maximum of 3 attempts. If both credentials are correct, print Login successful and stop. If all 3 attempts fail, print Account locked.
# Concepts: while, if/else, and, break, counting attempts


print("You have only 3 attempt so plz carefully")
i = 0 
while i < 3:
    print(i+1,"attempt")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "admin" and password == "12345":
       print("Login successful ")
       break
    else:
        print("Invalid username or password")
        i += 1
else:        
    print("Account Block")        

    

 
