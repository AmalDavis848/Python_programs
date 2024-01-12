from abc import ABC,abstractmethod

class Shape(ABC):
    def area(self):
        print("area of the shape")
    def perimeter(self):
        print("perimeter of shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length*self.length
    def perimeter(self):
        return 4*self.length
    
c=Circle(3)
s=Square(4)

print("circle area: ",c.area())
print("circle perimeter :",c.perimeter())