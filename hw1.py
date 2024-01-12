class Animal:
    def __init__(self,name):
        self.name=name

    def makeSound(self):
        print("crying")

class Dog(Animal):
     def makeSound(self):
        print("bow bow")

class Cat(Animal):
    def makeSound(self):
        print("meow meow")
a=Animal("amal")
myDog=Dog()
myCat=Cat()

def animalSounds(self):
    myDog.makeSound()
    myCat.makeSound()

