
#Planning

'''
1. Set an input to welcome new students
2. Ask if the user want to start (add a new student)
3. Please insert the GPA for each course
   a.If answers is "no" print students name
   b. if the user enters -1, student is done with its GPA
   c. if student doesnt enter any GPA, is in first semester
4.get the average from the GPA's
5.at the end show accumulative average GPAs

'''
print("Welcome to the Grade Registry Program")

students = {} #I created a dictionary empty to save all students
while True: 
  print("Would you like to add a new student?Yes/No")
   
  next_= input("").strip().lower()
  
  if next_ == "no":
    # Exit the loop if the user does not want to add a new student
    break
  
  #Continue the loop if the user asnwers yes
  
  elif next_ == "yes":
    #Ask for student (name)
    student = input ("Enter the student's name").strip()
    gpa_=[] #List for saving all GPAs
    
    print("Please enter student's GPA values")
    print("Type -1 when you finish, or press enter if the student is in first semester")

    while True: 
      gpa_input = input("GPA: ").strip
      #If the user do not respond
      if gpa_input == "":
        print("The student is in the first semester")
      #Break when the answer is -1
      elif gpa_input == "-1":
        break

  

  #ignore this "else for now"
  else:
   print('Please answer Yes or No')


