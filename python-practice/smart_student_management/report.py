import os
import sqlite3

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "students.db"
)
import sqlite3
import os

# Database Path
DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")


def student_report():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Total Students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Average Marks
    cursor.execute("SELECT AVG(marks) FROM students")
    average_marks = cursor.fetchone()[0]

    # Highest Marks
    cursor.execute("SELECT MAX(marks) FROM students")
    highest_marks = cursor.fetchone()[0]

    # Lowest Marks
    cursor.execute("SELECT MIN(marks) FROM students")
    lowest_marks = cursor.fetchone()[0]

    # Topper
    cursor.execute("""
        SELECT name, marks
        FROM students
        ORDER BY marks DESC
        LIMIT 1
    """)
    topper = cursor.fetchone()

    # Pass Count
    cursor.execute("SELECT COUNT(*) FROM students WHERE marks >= 35")
    pass_count = cursor.fetchone()[0]

    # Fail Count
    cursor.execute("SELECT COUNT(*) FROM students WHERE marks < 35")
    fail_count = cursor.fetchone()[0]

    # Grade Distribution
    cursor.execute("""
        SELECT grade, COUNT(*)
        FROM students
        GROUP BY grade
        ORDER BY grade
    """)
    grades = cursor.fetchall()

    connection.close()

    print("\n========== STUDENT DASHBOARD ==========\n")

    print(f"👨‍🎓 Total Students : {total_students}")

    if average_marks is not None:
        print(f"📊 Average Marks  : {average_marks:.2f}")
    else:
        print("📊 Average Marks  : 0")

    print(f"🏆 Highest Marks  : {highest_marks}")
    print(f"📉 Lowest Marks   : {lowest_marks}")

    if topper:
        print(f"🥇 Topper         : {topper[0]} ({topper[1]} Marks)")
    else:
        print("🥇 Topper         : No Students Found")

    print(f"✅ Pass Students  : {pass_count}")
    print(f"❌ Fail Students  : {fail_count}")

    print("\n====== Grade Distribution ======")

    if grades:
        for grade in grades:
            print(f"{grade[0]} : {grade[1]}")
    else:
        print("No grade data available.")