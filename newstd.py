import json
options = int(input("Enter (1) to view data,(2) to add,and (3) to delete : "))
if options == 1:
    with open("data/student.json", "r") as file:
      file= json.load(file)
      op = int(input("Enter 1 to search by ID or 2 to search by first name: "))
      if op == 1:
          roll = int(input("Enter the Roll ID of the student: "))
          found_students = [student for student in file["students"] if student["Roll_No."] == roll]
      elif op == 2:
          search_name = input("Enter first name to search: ")
          found_students = [student for student in file["students"] if student["first_name"].lower() == search_name.lower()]
  
      if found_students:
          print("Found student(s):")
          for student in found_students:
              print(f"{student['first_name']} {student['last_name']} ({student['current_class']}) | ID ({student['id']})" )
              print("<----STUDENT MARKS ---->")
              for i in student['marks']:
                  print(i ,end="-->")
                  print(student['marks'][i])
          for student in found_students:
              print("EMAILID---"+str(student['Email']),"MOBILE NO ---"+str(student['Mobile']) ,sep="\n")    
      else:
          print("No student found.")
elif options == 2:
    with open("data/student.json", "r") as file:
        std= json.load(file)
        new_student = {
        "id": len(std["students"]) + 1,
        "first_name": input("Enter first name: "),
        "last_name": input("Enter last name: "),
        "current_class": input("Enter current class: "),
        "Roll_No.":int(input("Enter Roll No. : ")),
        "marks":{"CS" : int(input("Enter The Computer Science marks :" )),
        "Maths" : int(input("Enter The Maths marks :" )),
        "Physics" : int(input("Enter The Physics marks :" )),
        "Yoga" : int(input("Enter The Yoga marks :" )),
        "English" : int(input("Enter The English marks :" )),
        },
        "Email":input("Enter Students Email :"),
        "Mobile":int(input("Enter The Students Mobile No :"))

    
        
    }
        std["students"].append(new_student)
    
    with open("data/student.json", "w") as file:
        json.dump( std,file, indent=2)
        


# Function to search for a student by first name or ID
elif options==3:
    with open("data/student.json", "r") as file:
        std= json.load(file)
        std["students"].pop(int(input("Enter the ID of Student to delete"))-1)
    with open("data/student.json","w") as file:
        json.dump(std,file,indent=2)   
        

else:
  print("Invalid choice. Please select a valid option.")    