class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(f"{self.brand} {self.model}")


car = Car("Toyota", "Innova")
car.show()