class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def emp_id(self,id):
        id=id
        print("employee name:=",self.name,"\nemployee age=:",self.age,"\nemployee id :",id)
e=Employee("amal",25)
e.emp_id(1001)