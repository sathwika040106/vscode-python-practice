import sqlite3
from tkinter import *

# Database Setup
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()

# Functions
def add_student():
    name = name_entry.get()
    marks = marks_entry.get()

    if name and marks:
        cursor.execute(
            "INSERT INTO students(name, marks) VALUES(?, ?)",
            (name, marks)
        )

        conn.commit()

        result.config(text="Student Added Successfully")

        name_entry.delete(0, END)
        marks_entry.delete(0, END)

def view_students():
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    output.delete("1.0", END)

    for row in records:
        output.insert(
            END,
            f"ID: {row[0]} | Name: {row[1]} | Marks: {row[2]}\n"
        )

# GUI
root = Tk()

root.title("Student Management System")
root.geometry("600x500")

Label(root, text="Student Name").pack(pady=5)

name_entry = Entry(root, width=40)
name_entry.pack()

Label(root, text="Marks").pack(pady=5)

marks_entry = Entry(root, width=40)
marks_entry.pack()

Button(
    root,
    text="Add Student",
    command=add_student
).pack(pady=10)

Button(
    root,
    text="View Students",
    command=view_students
).pack(pady=10)

result = Label(root, text="")
result.pack()

output = Text(root, height=15, width=60)
output.pack(pady=10)

root.mainloop()

conn.close()