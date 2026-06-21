import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

cursor.execute(
    "INSERT INTO students(name, marks) VALUES(?, ?)",
    (name, marks)
)

conn.commit()
conn.close()

print("Student Added Successfully")