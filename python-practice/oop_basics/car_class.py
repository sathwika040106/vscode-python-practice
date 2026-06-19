class Car:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)

c1 = Car("Honda")

c1.display()