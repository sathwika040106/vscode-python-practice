import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute(
    "INSERT INTO students(name, marks) VALUES(?, ?)",
    ("Sathwika", 95)
)

conn.commit()

print("Data Inserted Successfully")

conn.close()