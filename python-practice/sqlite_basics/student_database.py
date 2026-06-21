import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))

cursor.execute(
    "INSERT INTO students(name, marks) VALUES(?, ?)",
    (name, marks)
)

conn.commit()

print("Student Added Successfully")

cursor.execute("SELECT * FROM students")

print("\nStudent Records")

for row in cursor.fetchall():
    print(row)

conn.close()