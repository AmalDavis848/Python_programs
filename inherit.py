class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("welcome to inheritence")
class Dog(Animal):
    def speak(self):
        print("says wolf!!!",self.name)
class Cat(Animal):
    def speak(self):
        print("says meow!!!!",self.name)

d=Dog("puppy")
d.speak()
c=Cat("mammu")
c.speak()