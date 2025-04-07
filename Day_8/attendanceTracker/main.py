import Employee

employee=Employee.Employee()

user=True
while user:
  print("Please select the option below:")
  print("1.Create Employee")
  print("2.View All Employee")
  print("3.Mark Attendance")
  print("4.View Attendance")
  print("5.Generate Employee Report")
  print("6.Delete Employee")
  print("7.Exit")

  user_choice=int(input("enter your choice:"))

  if user_choice==1:
    employee_name=input("Enter Employee Name:")
    employee_age=input("Enter Age:")
    employee.create_employee(employee_name,employee_age)

  elif user_choice==2:
    employee.display_employee_all()

  elif user_choice==3:
    emp_id=int(input("Enter Employee id who is present:"))
    employee.mark_attendance(emp_id)

  elif user_choice==4:
    emp_name=input("Enter Employee ID whose attendance needs to be checked:")
    employee.view_attendance(employee.get_employee_id(emp_name))

  
  elif user_choice == 5:
    emp_name = input("Enter Employee name to generate report: ")
    emp_id = employee.get_employee_id(emp_name)
    employee.generate_report(emp_id)  

  elif user_choice==6:
    emp_name=input("Enter Employee name who is to be deleted:")
    employee.delete_employee(employee.get_employee_id(emp_name))

  elif user_choice==7:
    user=False
    break

  else:
    print("Invalid Number: Enter choice between 1 and 7.")
  

