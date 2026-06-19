class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

dog = Dog()
dog.sound()