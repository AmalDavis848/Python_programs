class Vehicle:
    def __int__(self,make,model):
        self.make=make
        self.model=model
    def start(self):
        print("press accelerator for start the vehicle")

    def stop(self):
        print("press brake for stop the vehicle")


class Car(Vehicle):
    def display():


    def num_doors(self):
        print("car has 4 doors","\nbrand is:",self.brand,"\nmodel=:",self.model)

class Motorcycle(Vehicle):

    def two_wheels(self):
        print("motor cycle has 2 wheels","\n brand :",self.brand,"\nprice=:",self.model)
"""
m=Motorcycle(2000,"pulsur 150")
m.two_wheels()
c=Car("Benz","fifty lakh")
c.num_doors()
#m.display()"""