import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "students.db")

connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\n===== STUDENT RECORDS =====\n")

for student in students:
    print(student)

connection.close()