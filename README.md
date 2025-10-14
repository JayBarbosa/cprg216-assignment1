# cprg216-assignment1
First Python assignment

Instructions
This assignment consists of the following sections, all completed outside of class time. See Brightspace for exact due date.

1. Working in a group, review the Scenario and the Grade Registry Program details sections of this document. (Planning, Analysis)
2. Draft a flowchart to represent the process/algorithm before writing the code of the program. (Design)
3. Write a program that meets the requirements described in the scenario above and prints the list of students with their corresponding accumulative GPAs. (Implementation)
4. When your program is complete, use the data listed in each of the following three tests below to see if your program works correctly. (Testing)

Note: Check your program against the marking criteria for the submission.

5. Your program’s output MUST EXACTLY MATCH the following tests.
6. Submit the following to Brightspace:

• The code of the program that you implemented (.py file)
• A copy of the output from your three test runs (.txt file)
• The flow chart in PDF format.
• Your GitHub repository for this assignment.

Grade Registry Program:

• The program uses the dictionary data structure to store students with their corresponding accumulative grades.
• The program asks the user if they want to add a student, if user answer with “yes” then the program asks the user to enter the GPAs for the student’s courses. If the user answers with "no”, the program prints the students’ names and exists.
• If the user enters -1, it means the user has finished inputting all the GPAs for the current student.
• After the user inputs all the GPAs, the average accumulative GPA is computed from the all the GPAs for all the courses taken by the student.
• If the user does not enter any GPA, it means a student is in the first semester and does not have any GPAs yet.
• Please use python lists with the append function to add new GPAs to the GPAs list. Obviously, there will be one list for each student. You can reuse the same list again for new students.
• Put the whole algorithm in a while loop to keep running until the user decides to exit the program (using the break statement).
• At the end of the program, the students’ names are printed with their corresponding accumulative average GPAs.

Grade Registry Program Tests:

Test 1
Welcome to the Grade Registry Program
Would you like to add a new student? y(yes),n(no)
yEs
Enter the student's name:
Sarah Gray
Enter student GPA for each subject. Enter -1 to stop entering GPA.
2.3
4.0
-1
Would you like to add a new student? y(yes),n(no)
Ya
Incorrect Input, please enter y(yes)/n(no).
Would you like to add a new student? y(yes),n(no)
Yes
Enter the student's name:
John Doe
Enter student GPA for each subject. Enter -1 to stop entering GPA.
3.2
3.9
2.5
-1
Would you like to add a new student? y(yes),n(no)
YEs
Enter the student's name:
Steven Grant
Enter student GPA for each subject. Enter -1 to stop entering GPA.
-1
Would you like to add a new student? y(yes),n(no)
n
This is the list of students in the system, and their corresponding accumulative GPA
Sarah Gray 3.15
John Doe 3.2
Steven Grant 0