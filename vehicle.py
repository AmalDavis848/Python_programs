class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def drive(self):
        print("i can drive car",self.brand,self.model)
class Motorcycle(Vehicle):
    def drive(self):
        print("i can drive motorcycle",self.brand,self.model)

m=Motorcycle("pulsor",220)
m.drive()
c=Car("benz","A class")
c.drive()