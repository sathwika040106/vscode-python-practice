import os
import sqlite3

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "students.db"
)
import sqlite3
import hashlib
import os

# ---------------- DATABASE PATH ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "students.db")


# ---------------- CONNECTION ----------------

def get_connection():
    return sqlite3.connect(DB_PATH)


# ---------------- CREATE TABLE ----------------

def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            marks INTEGER,
            grade TEXT,
            photo TEXT       
        
        )
    """)

    connection.commit()
    connection.close()


# ---------------- CREATE ADMIN TABLE ----------------

def create_admin_table():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    password = hashlib.sha256("admin123".encode()).hexdigest()

    cursor.execute("""
        INSERT OR  REPLACE INTO admin(id,username,password)
        VALUES(1,?,?)
    """, ("admin", password))

    connection.commit()
    connection.close()


# ---------------- ADD STUDENT ----------------

def add_student(student):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students(name,age,email,marks,grade,photo)
        VALUES(?,?,?,?,?,?)
    """, (
        student.name,
        student.age,
        student.email,
        student.marks,
        student.grade,
        student.photo
    ))

    connection.commit()
    connection.close()


# ---------------- VIEW STUDENTS ----------------

def view_students():
    

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY id
    """)

    students = cursor.fetchall()

    connection.close()

    return students
def get_all_students():
    return view_students()


# ---------------- UPDATE STUDENT ----------------

def update_student(student_id, student):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET
            name=?,
            age=?,
            email=?,
            marks=?,
            grade=?,
            photo=?
        WHERE id=?
    """, (
        student.name,
        student.age,
        student.email,
        student.marks,
        student.grade,
        student.photo,
        student_id
    ))

    connection.commit()
    connection.close()


# ---------------- DELETE STUDENT ----------------

def delete_student(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE id=?
    """, (student_id,))

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted > 0


# ---------------- SEARCH BY ID ----------------

def search_student_by_id(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        WHERE id=?
    """, (student_id,))

    student = cursor.fetchone()

    connection.close()

    return student
def search_student(keyword):
    return search_student_by_name(keyword)


# ---------------- SEARCH BY NAME ----------------

def search_student_by_name(name):
    def search_student(keyword):
     return search_student_by_name(keyword)

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        WHERE name LIKE ?
    """, ("%" + name + "%",))

    students = cursor.fetchall()

    connection.close()

    return students


# ---------------- SEARCH BY GRADE ----------------

def search_by_grade(grade):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        WHERE grade=?
    """, (grade,))

    students = cursor.fetchall()

    connection.close()

    return students


# ---------------- SEARCH BY MINIMUM MARKS ----------------

def search_by_min_marks(marks):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        WHERE marks>=?
    """, (marks,))

    students = cursor.fetchall()

    connection.close()

    return students


# ---------------- SEARCH BY MAXIMUM MARKS ----------------

def search_by_max_marks(marks):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        WHERE marks<=?
    """, (marks,))

    students = cursor.fetchall()

    connection.close()

    return students


# ---------------- STUDENT RANKING ----------------

def student_ranking():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM students
        ORDER BY marks DESC
    """)

    students = cursor.fetchall()

    connection.close()

    return students


# ---------------- INITIALIZE DATABASE ----------------

create_table()
create_admin_table()
def get_dashboard_data():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(marks) FROM students")
    average = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(marks) FROM students")
    highest = cursor.fetchone()[0]

    cursor.execute("SELECT MIN(marks) FROM students")
    lowest = cursor.fetchone()[0]

    connection.close()

    return {
        "total": total,
        "average": round(average, 2) if average else 0,
        "highest": highest if highest else 0,
        "lowest": lowest if lowest else 0
    }
def get_student_ranking():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            marks,
            grade
        FROM students
        ORDER BY marks DESC
    """)

    students = cursor.fetchall()

    connection.close()

    return students
def get_marks_data():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
    """)

    data = cursor.fetchall()

    connection.close()

    return data
def get_report_data():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            email,
            marks,
            grade
        FROM students
    """)

    students = cursor.fetchall()

    connection.close()

    return students
def get_csv_data():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            age,
            email,
            marks,
            grade
        FROM students
    """)

    students = cursor.fetchall()

    connection.close()

    return students
if __name__ == "__main__":

    print(get_all_students())




