# Job Eligibility Checker

# age = int(input("Enter Your age: "))
# education = input("Enter your graduation: ")
# experience = int(input("Enter your experience in years: "))

# if age >= 18 and education.upper() == "MCA":
#     if experience < 1:
#         print("You need at least one year of experience")
#     else:
#         print("Eligible to apply")
# elif age < 18 :
#     print("Plz apply next year")
# else:
#     print("You are not elegible")            





age = int(input("Enter Your age: "))
education = input("Enter your graduation: ")
experience = int(input("Enter your experience in years: "))

if age >= 18 and education.upper() == "MCA" and experience >=1:
    print("You are elegilbe")
elif age < 18 or education.upper() != "MCA" or experience < 1:
    print("Not Elegible")    
else :
    print("Somethimg else")     

