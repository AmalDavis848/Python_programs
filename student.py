class Student:
    def __init__(self,name,phno,address):
        self.name=name
        self.phno=phno
        self.address=address
        
    def display(self):
        print("student name is :",self.name,"\n student phno is :",self.phno,"\n student address is :",self.address)


stud=Student("arun",9876543210,"menachery house kaprassery")
stud.display()