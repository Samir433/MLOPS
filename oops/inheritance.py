# Simple inheritance

# parent class
class Animal:
    def __init__(self, name):
        print("Constructor of the parent class called")
        self.name = name
    
    def speak(self):
        print("Speak method of the parent class called")
        print(f"{self.name} make a sound")
    

# child class
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Domestic Animals"
    
    def speak(self):
        super().speak()
        print(f"{self.name} barks and the type of the {self.name} is {self.type}")

dog = Dog("Fantya")
dog.speak()

#  hybrid inheritance 
class A:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        print("Hello From the class B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from the class C")
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from the class D")
        super().greet()

obj = D("Don")
obj.greet()