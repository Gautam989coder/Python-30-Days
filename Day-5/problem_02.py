# Student Grade Calculator
# Create a function calculate_average(marks) that accepts a list of marks and returns the average.

# Then create get_grade(average) that returns a grade using these rules:
# - 90 or more: A
# - 75 or more: B
# - 60 or more: C
# - 33 or more: D
# - Below 33: Fail
# Test both functions with a list of five subject marks.


def calculate_average(marks):
    average = sum(marks)//len(marks)
    return average
        
def get_grade(average):
    if average >= 90:
        return "Grade: A" 
    elif average >= 80:
        return "Grade: B"
    elif average >= 70:
        return "Grade: C"
    elif average >= 60:
        return"Grade: D"
    elif average >= 33:
        return "Grade: E"
    else:
        return "Fail"
  
    
student1 = [70, 80, 80, 90, 90]
s1 = calculate_average(student1)
print(s1)
s2 = get_grade(s1)
print(s2)


student2 = [55, 47, 66, 45, 34]
s2 = calculate_average(student2)
print(s2)
s3 = get_grade(s2)
print(s3)