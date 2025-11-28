
def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    choice = input()
    return choice

def add(students, student_id, name, gpa, semester):
    student = [student_id, name, gpa, semester]
    students.append(student)
    print("Student added")
    print(student_id, name, gpa, semester)

def remove(students, student_id):
    for student in students:
        if student[0] == student_id:
            students.remove(student)
            print("Student removed")
            return
    print("Student not found")

def edit_name(students, student_id, new_name):
    for student in students:
        if student[0] == student_id:
            student[1] = new_name
            print(f"Student name modified for the student with id {student_id}")
            print(f"Student's new name is {new_name}")
            return
    print("Student not found")

def search(students, student_id):
    for student in students:
        if student[0] == student_id:
            print("Student found")
            print(student[0], student[1], student[2])
            return True
    print("Student not found")
    return False

def run_search(students):
    while True:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        student_id = input()
        
        if student_id == "-1":
            break
        
        search(students, student_id)

def run_edit(students):
    while True:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        student_id = input()
        
        if student_id == "-1":
            break
        
        print("Enter the new name of the student")
        new_name = input()
        edit_name(students, student_id, new_name)

def run_add(students):
    while True:
        print("Enter id of the student, followed by the student's information.")
        print("id:")
        student_id = input()
        print("name:")
        name = input()
        print("gpa:")
        gpa = float(input())
        print("semester:")
        semester = int(input())
        
        add(students, student_id, name, gpa, semester)
        
        print("Do you want to add a new student?y(yes)/n(no)")
        choice = input()
        if choice.lower() == "n" or choice.lower() == "no":
            break

def run_remove(students):
    while True:
        print("Enter id of the student that you want to remove from the students' registry.")
        print("id:")
        student_id = input()
        
        remove(students, student_id)
        
        print("Do you want to remove more students?y(yes)/n(no)", end="")
        choice = input()
        if choice.lower() == "n" or choice.lower() == "no":
            break

# Main program
def main():
    # List to store all students
    students = []
    
    # Welcome message
    print("Welcome to the students record program")
    
    # Main loop
    while True:
        # Show menu and get user choice
        choice = show_menu()
        
        # Process user choice
        if choice == "1":
            run_search(students)
        elif choice == "2":
            run_edit(students)
        elif choice == "3":
            run_add(students)
        elif choice == "4":
            run_remove(students)
        
        # Ask if user wants to continue
        print("What you like to continue(y/yes), or exit the program(n/no)?")
        continue_choice = input()
        if continue_choice.lower() == "n" or continue_choice.lower() == "no":
            break
# Run the main program
main()