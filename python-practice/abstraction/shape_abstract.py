from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def area(self):
        print(10 * 5)

r = Rectangle()
r.area()