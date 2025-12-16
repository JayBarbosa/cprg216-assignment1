
class Student:
    #Class to represent a student with their enrollment information
    
    def __init__(self, student_id, first_name, last_name, gpa, semester):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.semester = semester
    
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.gpa} {self.semester}"
    
    def to_file_string(self):
        #Convert student data to string format for file storage
        return f"{self.id},{self.first_name},{self.last_name},{self.gpa},{self.semester}\n"


# Global student list
students = []


def load_data():
    #Load student data from data.txt file
    global students
    try:
        with open("data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    student = Student(int(parts[0]), parts[1], parts[2], 
                                    float(parts[3]), int(parts[4]))
                    students.append(student)
    except FileNotFoundError:
        pass  


def save_data():
    #Save student data to data.txt file
    with open("data.txt", "w") as file:
        for student in students:
            file.write(student.to_file_string())
    print("Data saved to local file successfully!")


def find_student_by_id(student_id):
    #Find and return a student by their ID
    for student in students:
        if student.id == student_id:
            return student
    return None


def find_student_by_name(first_name, last_name):
    #Find and return a student by their name
    for student in students:
        if student.first_name == first_name and student.last_name == last_name:
            return student
    return None


def add_student():
    #Add new students to the system
    while True:
        print("Enter id of the student, followed by the student's information.")
        
        student_id = int(input("Id:\n"))
        first_name = input("First name:\n")
        last_name = input("Last name:\n")
        gpa = float(input("GPA:\n"))
        semester = int(input("Semester:\n"))
        
        # Check if ID already exists
        if find_student_by_id(student_id):
            print("Incorrect Id. Id already exist in the system.")
        # Check if student with same name already exists
        elif find_student_by_name(first_name, last_name):
            print("The student already enrolled. No action is required..")
        else:
            # Add new student
            new_student = Student(student_id, first_name, last_name, gpa, semester)
            students.append(new_student)
            print("Student Enrolled in the system")
            print(new_student)
        
        # Ask if user wants to add more
        choice = input("Do you want to add more students? y(yes)/n(no)\n")
        if choice.lower() == 'n':
            break


def search_student():
    while True:
        print("To search using the Id enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu")
        choice = int(input())
        
        if choice == -1:
            break
        elif choice == 1:
            student_id = int(input("Please Enter the id of the student:\n"))
            student = find_student_by_id(student_id)
            if student:
                print(f"Student found {student}")
            else:
                print("Student not found")
        elif choice == 2:
            first_name = input("Please Enter the first name of the student:\n")
            last_name = input("Please Enter the last name of the student:\n")
            student = find_student_by_name(first_name, last_name)
            if student:
                print(f"Student found {student}")
            else:
                print("Student not found")


def edit_student():
    #Edit student information
    while True:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        student_id = int(input())
        
        if student_id == -1:
            break
        
        student = find_student_by_id(student_id)
        if student:
            student.first_name = input("First name:\n")
            student.last_name = input("Last name:\n")
            student.gpa = float(input("GPA:\n"))
            student.semester = int(input("Semester:\n"))
            print(f"Student's new info is {student}")
        else:
            print("Student not found")


def remove_student():
    #Remove a student from the system
    while True:
        print("Enter id of the student that you want to remove from the students' registry.")
        student_id = int(input("id:\n"))
        
        student = find_student_by_id(student_id)
        if student:
            students.remove(student)
            print("Student removed")
        else:
            print("Student not found")
        
        choice = input("Do you want to remove more students?y(yes)/n(no)")
        if choice.lower() == 'n':
            break


def print_student_list():
    #Print all students in the system
    for student in students:
        print(student)


def show_menu():
    #Display the main menu
    print("\nWhat would you like to do today?")
    print("-Add a student? enter 1")
    print("-Search for student 2")
    print("-Edit student info? enter 3")
    print("-Remove a student? enter 4")
    print("-Print the student list? enter 5")
    print("-Save the data to a file? enter 6")


def main():
    #Main function to run the student enrollment system
    # Load existing data
    load_data()
    
    print("Welcome to the Students Enrollment system")
    
    while True:
        show_menu()
        choice = int(input())
        
        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            edit_student()
        elif choice == 4:
            remove_student()
        elif choice == 5:
            print_student_list()
        elif choice == 6:
            save_data()
        
        # Ask if user wants to continue
        continue_choice = input("What you like to continue(y/yes), or exit the program(n/no)?\n")
        if continue_choice.lower() == 'n' or continue_choice.lower() == 'no':
            break


if __name__ == "__main__":
    main()
    