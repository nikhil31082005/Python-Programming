student_present = 0
student_absent = 0

while True:
    name = input("Enter the name of the student or type done to exit: ")
    if name == "done":
        break
    attendence = input("Is student present or absent ")
    if attendence == 'present':
        student_present = student_present + 1
    else:
        student_absent = student_absent + 1
print(f'Number of present student is {student_present}')
print(f'Number of absent student is {student_absent}')