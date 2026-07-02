import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

print("DATABASE:", DB_PATH)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", cursor.fetchall())

cursor.execute("SELECT * FROM admin")
print("Admin Table:", cursor.fetchall())

connection.close()