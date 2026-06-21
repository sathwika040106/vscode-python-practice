import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

student_id = int(input("Enter Student ID: "))
new_marks = int(input("Enter New Marks: "))

cursor.execute(
    "UPDATE students SET marks=? WHERE id=?",
    (new_marks, student_id)
)

conn.commit()
conn.close()

print("Record Updated Successfully")