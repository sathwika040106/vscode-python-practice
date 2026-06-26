class Bird:
    def sound(self):
        print("Bird chirps")


class Cat:
    def sound(self):
        print("Cat meows")


animals = [Bird(), Cat()]

for animal in animals:
    animal.sound()