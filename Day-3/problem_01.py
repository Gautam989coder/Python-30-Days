# Login System


# username = input("enter username name: ")
# password = int(input("enter your password: "))

# # print(username.upper()[0])

# if username == "user123" and password == 1234567 :
#    print("Login Succesfull")
# else:
#    print("Invalid username and passward") 
# #========================================================================   


# user2 = input("enter useranme: ")
# password2 = input("enter password: ")  

i = 0
while i < 3:
   user2 = input("enter useranme: ")
   password2 = input("enter password: ")  
   if user2 == "user" and password2 == "1234":
      print("login successfull") 
      break
   else:
      print("failed")   
      i += 1 
else:
   print("account locked!")     