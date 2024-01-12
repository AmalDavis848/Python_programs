class Employee:
    def __init__(self):
        print("employee details")
    def display(self,name,code,salary):
        self.name=name
        self.code=code
        self.salary=salary
        print("employ name is :",self.name,"\nemployee code is :",self.code,"\nemployee salary is :",self.salary)
emp=Employee()

n=input("enter the name of employee")
c=int(input("enter the employee code"))
sal=int(input("enter the employee salary"))
emp.display(n,c,sal)