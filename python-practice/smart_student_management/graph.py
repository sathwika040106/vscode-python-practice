import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------- DATABASE PATH ----------------

DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "students.db"
)


def get_connection():
    return sqlite3.connect(DB_PATH)


# ---------------- BAR CHART ----------------

def bar_chart():

    connection = get_connection()

    df = pd.read_sql_query(
        "SELECT name, marks FROM students ORDER BY marks DESC",
        connection
    )

    connection.close()

    if df.empty:
        print("❌ No Student Data Found.")
        return

    plt.figure(figsize=(10,5))

    plt.bar(df["name"], df["marks"])

    plt.title("Student Marks")

    plt.xlabel("Students")

    plt.ylabel("Marks")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


# ---------------- LINE CHART ----------------

def line_chart():

    connection = get_connection()

    df = pd.read_sql_query(
        "SELECT name, marks FROM students ORDER BY id",
        connection
    )

    connection.close()

    if df.empty:
        print("❌ No Student Data Found.")
        return

    plt.figure(figsize=(10,5))

    plt.plot(
        df["name"],
        df["marks"],
        marker="o",
        linewidth=2
    )

    plt.title("Student Marks Trend")

    plt.xlabel("Students")

    plt.ylabel("Marks")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


# ---------------- PIE CHART ----------------

def pie_chart():

    connection = get_connection()

    df = pd.read_sql_query(
        """
        SELECT grade, COUNT(*) AS total
        FROM students
        GROUP BY grade
        """,
        connection
    )

    connection.close()

    if df.empty:
        print("❌ No Student Data Found.")
        return

    plt.figure(figsize=(6,6))

    plt.pie(
        df["total"],
        labels=df["grade"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Grade Distribution")

    plt.axis("equal")

    plt.show()