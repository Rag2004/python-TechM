from datetime import date,timedelta,datetime

class Employee:
    Employee_dict={}
    count=1000

    def create_employee(self,name,age):
        self.count+=1
        employee={
            'Emp_id':self.count,
            'name':name,
            'age':age
        }
        print("Employee Created Successfully: Employee ID",employee['Emp_id'])
        self.Employee_dict[self.count] = employee 

    def display_employee_all(self):
        for emp_id,employee in self.Employee_dict.items():
            print(f"emp_id:{employee['Emp_id']},name:{employee['name']},age:{employee['age']}")    

    def get_employee_id(self,name):
        for emp_id,employee in self.Employee_dict.items():
            employee['name']==name
            return employee['Emp_id']
    
    def delete_employee(self,emp_id):
        del self.Employee_dict[emp_id]
        print("Employee deleted successfully")

    def view_attendance(self,emp_id):
        employee_found=False
        for employee in self.Employee_dict.values():
            if employee['Emp_id']==emp_id:
                last_7_days=[]
                today=datetime.today().date()

                for record in employee.get('attendance',[]):
                     record_date = datetime.strptime(record['date'], "%Y-%m-%d").date()
                     if today-timedelta(days=7)<=record_date<=today:
                         last_7_days.append(record)
                if last_7_days:
                    print(f"Last Seven days attendance of {employee['name']}:{last_7_days}")
                else:
                    print(f"No attendance record found for {employee['name']}")

                return last_7_days 

        if not employee_found:
            print("Employee not found")
            return None

    def mark_attendance(self, emp_id):
        for employee in self.Employee_dict.values():
            if employee['Emp_id'] == emp_id:
                if 'attendance' not in employee:
                    employee['attendance'] = []
    
                emp_attendance = employee['attendance']
                last_seven_date = date.today() - timedelta(days=7)
    
                for i in range(7):
                    current_date = last_seven_date + timedelta(days=i)
                    attendance = input(
                        f"Enter attendance for {current_date} ('p' for present, 'a' for absent): "
                    ).strip().lower()
    
                    if attendance not in ['p', 'a']:
                        print("Invalid input. Skipping.")
                        continue
    
                    daily_record = {
                        'date': str(current_date),
                        'attendance': attendance
                    }
                    emp_attendance.append(daily_record)
    
                print("Attendance marked successfully.")
                return
    
        print("Employee not found.")
    
    def generate_report(self, emp_id):
        employee_found = False
        for employee in self.Employee_dict.values():
            if employee['Emp_id'] == emp_id:
                employee_found = True
                today = datetime.today().date()
                last_7_days = []
    
                for record in employee.get('attendance', []):
                    record_date = datetime.strptime(record['date'], "%Y-%m-%d").date()
                    if today - timedelta(days=7) <= record_date <= today:
                        last_7_days.append(record)
    
                last_7_days.sort(key=lambda x: x['date'])
    
                consecutive_absent = 0
                for rec in last_7_days:
                    if rec['attendance'] == 'a':
                        consecutive_absent += 1
                        if consecutive_absent >= 3:
                            print(f"Employee {employee['name']} (ID: {employee['Emp_id']}) needs attention ")
                            return "Needs Attention"
                    else:
                        consecutive_absent = 0  
    
                print(f"Employee {employee['name']} (ID: {employee['Emp_id']}) is doing good ")
                return "All Good"
    
        if not employee_found:
            print("Employee not found")
            return "Employee not found"
    