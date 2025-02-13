"""  Create a mini-project where students combine conditional statements, loops, and functions
to create a basic Python application, such as a simple calculator or a grade management system."""

def Calc_grade(per):
    if per >= 90:
        return 'A'
    elif per >= 80:
        return 'B'
    elif per >= 70:
        return 'C'
    elif per >= 60:
        return 'D'
    else:
        return 'F'

print("--------------------------------------------------")
    
def add_student():
    R = int(input("Enter Your Rollno : "))
    S = input("Enter Your Name : ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter Your Marks in Subject {i} : "))
        marks.append(mark)

    Result = sum(marks)
    per = (Result / 500) * 100
    grade = Calc_grade(per)

    return R, S, marks, Result, per, grade

def Display(R, S, marks, Result, per, grade):
    print("\n------------------- Marksheet -------------------")
    print(f"Roll Number: {R}")
    print(f"Student Name: {S}")
    print("Subject Marks: ")
    print("--------------------------------------------------")
    for i in range(5):
        print(f"Subject {i+1}: {marks[i]}") 
    print("--------------------------------------------------")
    print(f"Percentage: {per}%")
    print(f"Grade: {grade}")
    print("--------------------------------------------------")  
R, S, marks, Result, per, grade = add_student()
Display(R, S, marks, Result, per, grade)