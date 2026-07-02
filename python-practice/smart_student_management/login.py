import sqlite3
import hashlib
import os

# ---------------- DATABASE PATH ----------------

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "students.db"
)

# ---------------- LOGIN FUNCTION ----------------

def login():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    print("\n========== ADMIN LOGIN ==========\n")

    username = input("Username : ").strip()
    password = input("Password : ").strip()

    # Encrypt password
    password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("""
        SELECT *
        FROM admin
        WHERE username = ?
        AND password = ?
    """, (username, password))

    admin = cursor.fetchone()

    connection.close()

    if admin:
        print("\n✅ Login Successful!")
        return True

    else:
        print("\n❌ Invalid Username or Password!")
        return False