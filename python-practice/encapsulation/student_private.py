class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def show_marks(self):
        print("Marks =", self.__marks)

s = Student("Sathwika", 95)

print(s.name)
s.show_marks()