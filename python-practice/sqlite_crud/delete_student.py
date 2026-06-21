import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

student_id = int(input("Enter Student ID to Delete: "))

cursor.execute(
    "DELETE FROM students WHERE id=?",
    (student_id,)
)

conn.commit()
conn.close()

print("Record Deleted Successfully")