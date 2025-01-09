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