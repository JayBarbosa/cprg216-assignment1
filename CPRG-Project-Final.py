def new_func():
    '''
. Set an input to welcome new students
2. Ask if the user want to start (add a new student)
3. Please insert the GPA for each course
   a.If answers is "no" print students name
   b. if the user enters -1, student is done with its GPA
   c. if student doesnt enter any GPA, is in first semester
4.get the average from the GPA's
5.at the end show accumulative average GPAs
'''

print("Welcome to the Grade Registry Program")

student_list = {}
def add_student():
    student_name = input("Enter the student's name: ").strip()
    
def add_gpatostudent():
    print("Please enter the student's GPA values.")
    print("Type -1 when you finish, or press enter if the student is in their first semester.")
    while True:
            gpa_input = input("GPA: ").strip()
            
            if gpa_input == "":
                print("The student is in their first semester.")
                break
            elif gpa_input == "-1":
                break
            else:
                try:
                    gpa_value = float(gpa_input)
                    if 0.0 <= gpa_value <= 4.0:
                        gpa_list.append(gpa_value)
                    else:
                        print("Please enter a valid GPA between 0.0 and 4.0.")
                except ValueError:
                    print("Invalid input. Please enter a numeric GPA value.")
def view_gpa_list():
    print("All registered students and their average GPAs:")
    for name, avg_gpa in student_list.items():
        print(f"{name}'s average GPA is {avg_gpa:.2f}")
while True:
    new_student = input("Would you like to register a new student? Yes/No: ").strip().lower()
     
    if new_student == "no":
         break
    elif new_student == "yes":
        add_student()
        # start a fresh GPA list for this student so previous entries don't carry over
        gpa_list = []
        add_gpatostudent()
        if gpa_list:
            average_gpa = sum(gpa_list) / len(gpa_list)
            student_list[student_name] = average_gpa
            print(f"{student_name}'s average GPA is {average_gpa:.2f}")
        else:
            print(f"{student_name} has no GPA records.")

view_gpa_list()