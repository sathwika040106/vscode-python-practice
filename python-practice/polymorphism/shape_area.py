class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print(10 * 5)

class Square(Shape):
    def area(self):
        print(5 * 5)

Rectangle().area()
Square().area()