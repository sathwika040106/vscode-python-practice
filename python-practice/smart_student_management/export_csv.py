import sqlite3
import pandas as pd
import os

# Database Path
DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")


def export_students():

    connection = sqlite3.connect(DB_PATH)

    query = """
        SELECT *
        FROM students
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    if df.empty:
        print("❌ No Student Data Found.")
        return

    file_name = "students_report.csv"

    df.to_csv(file_name, index=False)

    print(f"\n✅ CSV Exported Successfully!")
    print(f"📄 File Saved As : {file_name}")