import csv

students = [
    ["Name", "Marks"],
    ["Sathwika", 95],
    ["Anu", 88],
    ["Ravi", 91]
]

with open("student_marks.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(students)

print("Student records saved")