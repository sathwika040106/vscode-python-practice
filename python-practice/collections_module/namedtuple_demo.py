from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

s1 = Student("Sathwika", 21)

print(s1.name)
print(s1.age)