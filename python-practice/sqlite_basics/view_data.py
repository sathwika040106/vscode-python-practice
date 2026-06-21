import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for row in records:
    print(row)

conn.close()