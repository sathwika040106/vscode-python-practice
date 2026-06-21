import sqlite3

conn = sqlite3.connect("students.db")

print("Database Created Successfully")

conn.close()