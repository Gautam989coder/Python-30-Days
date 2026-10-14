# Student Result System

# math = int(input("Enter Your maths mark: "))
# eng = int(input("Enter Your english mark: "))
# art = int(input("Enter Your arts mark: "))
# hindi = int(input("Enter Your hindi mark: "))
# sst = int(input("Enter Your social science mark: "))

# total_marks = math + eng + art + hindi + sst
# marks_avg = total_marks//5
# persentage = total_marks*100//500

# print(f'Total Marks: {total_marks} / 500')
# print(f'Marks Avarage: {marks_avg}')
# print(f'Percentage: {persentage}%')

# if persentage >= 90 :
#     print(f'Result pass \nGrade: A+')
# elif persentage >= 80 :
#     print(f'Result pass \nGrade: A')
# elif persentage >= 70 :
#     print(f'Result pass \nGrade: B+')
# elif persentage >= 60:
#     print(f'Result pass \nGrade: B') 
# elif persentage >= 50:
#     print(f'Result pass \nGrade: c')       
# else :
#     print("Result: fail")






math = int(input("Enter Your maths mark: "))
eng = int(input("Enter Your english mark: "))
art = int(input("Enter Your arts mark: "))
hindi = int(input("Enter Your hindi mark: "))
sst = int(input("Enter Your social science mark: "))

marks = [math, eng, art, hindi, sst]
valid_marks = True

for mark in marks:
    if mark < 0 or mark > 100:
        print("Invalid marks! Marks must be between 0 and 100.")
        valid_marks = False
        break

if valid_marks:
    total_marks = sum(marks)
    avg = total_marks/len(marks)
    percentage = total_marks*100/500

    print(f'Total Marks: {total_marks} / 500')
    print(f'Marks Avarage: {avg}')
    print(f'Percentage: {percentage}%')    


    for mark in marks: 
        if mark < 33:
          print("Result: Fail")
          break
    else:
        if percentage >= 90 :
           print(f'Result pass \nGrade: A+')
        elif percentage >= 80 :
           print(f'Result pass \nGrade: A')
        elif percentage >= 70 :
           print(f'Result pass \nGrade: B+')
        elif percentage >= 60:
           print(f'Result pass \nGrade: B') 
        elif percentage >= 50:
           print(f'Result pass \nGrade: C')       
        else :
           print("Result: Pass")
           print("Grade: D")

