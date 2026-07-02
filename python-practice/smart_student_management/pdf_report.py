import sqlite3
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Database Path
DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")


def generate_pdf():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, age, email, marks, grade
        FROM students
        ORDER BY id
    """)

    students = cursor.fetchall()

    connection.close()

    if len(students) == 0:
        print("❌ No Student Data Found.")
        return

    pdf = SimpleDocTemplate("Student_Report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>SMART STUDENT MANAGEMENT REPORT</b>",
            styles["Title"]
        )
    )

    table_data = [
        ["ID", "Name", "Age", "Email", "Marks", "Grade"]
    ]

    for student in students:
        table_data.append(student)

    table = Table(table_data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("GRID", (0,0), (-1,-1), 1, colors.black),

        ("BACKGROUND", (0,1), (-1,-1), colors.beige),

        ("ALIGN", (0,0), (-1,-1), "CENTER"),

        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0,0), (-1,0), 10)

    ]))

    elements.append(table)

    pdf.build(elements)

    print("\n✅ PDF Report Generated Successfully!")