class Student:

    school = "ABC High School"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")
        print(f"School: {Student.school}")


s1 = Student("Sathwika")
s2 = Student("Rahul")

s1.display()
s2.display()