from dataclasses import dataclass


@dataclass
class Student:
    name: str
    marks: int


student = Student("Sathwika", 95)

print(student)