from student import Student

from database import (
    add_student,
    view_students,
    update_student,
    delete_student,
    search_student_by_id,
    search_student_by_name,
    search_by_grade,
    search_by_min_marks,
    search_by_max_marks,
    student_ranking
)

from validations import (
    validate_name,
    validate_age,
    validate_email,
    validate_marks,
    calculate_grade
)

from logger import log_info
from export_csv import export_students
from report import student_report

from graph import (
    bar_chart,
    line_chart,
    pie_chart
)

from pdf_report import generate_pdf
from backup import backup_database, restore_database
from login import login
from utils import clear_screen, pause


# ---------------- LOGIN ----------------

if not login():
    exit()


# ---------------- MAIN LOOP ----------------

while True:

    clear_screen()

    print("\n========== SMART STUDENT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Export Students to CSV")
    print("7. Student Dashboard")
    print("8. Graph Analytics")
    print("9. Generate PDF Report")
    print("10. Student Ranking")
    print("11. Backup Database")
    print("12. Restore Database")
    print("13. Exit")

    choice = input("\nEnter Choice : ")

    # ===================================================
    # ADD STUDENT
    # ===================================================

    if choice == "1":

        print("\n------ ADD STUDENT ------")

        name = input("Enter Name : ")

        if not validate_name(name):
            print("❌ Invalid Name!")
            pause()
            continue

        try:
            age = int(input("Enter Age : "))
        except ValueError:
            print("❌ Age must be a number.")
            pause()
            continue

        if not validate_age(age):
            print("❌ Invalid Age.")
            pause()
            continue

        email = input("Enter Email : ")

        if not validate_email(email):
            print("❌ Invalid Email.")
            pause()
            continue

        try:
            marks = int(input("Enter Marks : "))
        except ValueError:
            print("❌ Marks must be a number.")
            pause()
            continue

        if not validate_marks(marks):
            print("❌ Marks should be between 0 and 100.")
            pause()
            continue

        grade = calculate_grade(marks)

        student = Student(
            name,
            age,
            email,
            marks,
            grade
        )

        add_student(student)

        log_info(f"Student Added : {name}")

        print("\n✅ Student Added Successfully!")

        pause()
            # ===================================================
    # VIEW STUDENTS
    # ===================================================

    elif choice == "2":

        students = view_students()

        print("\n========== STUDENT LIST ==========\n")

        if len(students) == 0:

            print("No Students Found.")

        else:

            print(
                f"{'ID':<5}"
                f"{'NAME':<20}"
                f"{'AGE':<8}"
                f"{'EMAIL':<30}"
                f"{'MARKS':<10}"
                f"{'GRADE'}"
            )

            print("-" * 90)

            for student in students:

                print(
                    f"{student[0]:<5}"
                    f"{student[1]:<20}"
                    f"{student[2]:<8}"
                    f"{student[3]:<30}"
                    f"{student[4]:<10}"
                    f"{student[5]}"
                )

        pause()


    # ===================================================
    # UPDATE STUDENT
    # ===================================================

    elif choice == "3":

        print("\n------ UPDATE STUDENT ------")

        try:
            student_id = int(input("Enter Student ID : "))
        except ValueError:
            print("❌ Invalid Student ID")
            pause()
            continue

        name = input("Enter New Name : ")

        if not validate_name(name):
            print("❌ Invalid Name")
            pause()
            continue

        try:
            age = int(input("Enter New Age : "))
        except ValueError:
            print("❌ Invalid Age")
            pause()
            continue

        if not validate_age(age):
            print("❌ Age should be between 5 and 100")
            pause()
            continue

        email = input("Enter New Email : ")

        if not validate_email(email):
            print("❌ Invalid Email")
            pause()
            continue

        try:
            marks = int(input("Enter New Marks : "))
        except ValueError:
            print("❌ Invalid Marks")
            pause()
            continue

        if not validate_marks(marks):
            print("❌ Marks should be between 0 and 100")
            pause()
            continue

        updated = update_student(
            student_id,
            name,
            age,
            email,
            marks
        )

        if updated:

            log_info(f"Student Updated : {student_id}")

            print("\n✅ Student Updated Successfully!")

        else:

            print("\n❌ Student Not Found!")

        pause()


    # ===================================================
    # DELETE STUDENT
    # ===================================================

    elif choice == "4":

        print("\n------ DELETE STUDENT ------")

        try:
            student_id = int(input("Enter Student ID : "))
        except ValueError:
            print("❌ Invalid Student ID")
            pause()
            continue

        confirm = input("Are you sure? (Y/N): ").upper()

        if confirm == "Y":

            deleted = delete_student(student_id)

            if deleted:

                log_info(f"Student Deleted : {student_id}")

                print("\n✅ Student Deleted Successfully!")

            else:

                print("\n❌ Student Not Found!")

        else:

            print("\nDeletion Cancelled.")

        pause()
            # ===================================================
    # SEARCH STUDENT
    # ===================================================

    elif choice == "5":

        print("\n------ SEARCH STUDENT ------")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Search by Grade")
        print("4. Search by Minimum Marks")
        print("5. Search by Maximum Marks")

        search_choice = input("\nEnter Choice : ")

        # -------- Search by ID --------
        if search_choice == "1":

            try:
                student_id = int(input("Enter Student ID : "))
            except ValueError:
                print("❌ Invalid Student ID")
                pause()
                continue

            student = search_student_by_id(student_id)

            if student:

                print("\n========== STUDENT DETAILS ==========")
                print(f"ID     : {student[0]}")
                print(f"Name   : {student[1]}")
                print(f"Age    : {student[2]}")
                print(f"Email  : {student[3]}")
                print(f"Marks  : {student[4]}")
                print(f"Grade  : {student[5]}")

            else:
                print("\n❌ Student Not Found!")

        # -------- Search by Name --------
        elif search_choice == "2":

            name = input("Enter Student Name : ")

            students = search_student_by_name(name)

            if students:

                print(f"\n{'ID':<5}{'NAME':<20}{'MARKS':<10}{'GRADE'}")
                print("-" * 50)

                for student in students:

                    print(
                        f"{student[0]:<5}"
                        f"{student[1]:<20}"
                        f"{student[4]:<10}"
                        f"{student[5]}"
                    )

            else:
                print("\n❌ Student Not Found!")

        # -------- Search by Grade --------
        elif search_choice == "3":

            grade = input("Enter Grade : ").upper()

            students = search_by_grade(grade)

            if students:

                print(f"\n{'ID':<5}{'NAME':<20}{'MARKS':<10}{'GRADE'}")
                print("-" * 50)

                for student in students:

                    print(
                        f"{student[0]:<5}"
                        f"{student[1]:<20}"
                        f"{student[4]:<10}"
                        f"{student[5]}"
                    )

            else:
                print("\n❌ No Students Found!")

        # -------- Search by Minimum Marks --------
        elif search_choice == "4":

            marks = int(input("Enter Minimum Marks : "))

            students = search_by_min_marks(marks)

            if students:

                print(f"\n{'ID':<5}{'NAME':<20}{'MARKS':<10}{'GRADE'}")
                print("-" * 50)

                for student in students:

                    print(
                        f"{student[0]:<5}"
                        f"{student[1]:<20}"
                        f"{student[4]:<10}"
                        f"{student[5]}"
                    )

            else:
                print("\n❌ No Students Found!")

        # -------- Search by Maximum Marks --------
        elif search_choice == "5":

            marks = int(input("Enter Maximum Marks : "))

            students = search_by_max_marks(marks)

            if students:

                print(f"\n{'ID':<5}{'NAME':<20}{'MARKS':<10}{'GRADE'}")
                print("-" * 50)

                for student in students:

                    print(
                        f"{student[0]:<5}"
                        f"{student[1]:<20}"
                        f"{student[4]:<10}"
                        f"{student[5]}"
                    )

            else:
                print("\n❌ No Students Found!")

        else:

            print("\n❌ Invalid Choice!")

        pause()


    # ===================================================
    # EXPORT CSV
    # ===================================================

    elif choice == "6":

        export_students()

        log_info("CSV Exported Successfully")

        pause()


    # ===================================================
    # STUDENT DASHBOARD
    # ===================================================

    elif choice == "7":

        student_report()

        pause()


    # ===================================================
    # GRAPH ANALYTICS
    # ===================================================

    elif choice == "8":

        print("\n====== GRAPH MENU ======")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart")

        graph_choice = input("\nEnter Choice : ")

        if graph_choice == "1":
            bar_chart()

        elif graph_choice == "2":
            line_chart()

        elif graph_choice == "3":
            pie_chart()

        else:
            print("❌ Invalid Choice!")

        pause()
            # ===================================================
    # GENERATE PDF REPORT
    # ===================================================

    elif choice == "9":

        generate_pdf()

        log_info("PDF Report Generated")

        pause()


    # ===================================================
    # STUDENT RANKING
    # ===================================================

    elif choice == "10":

        students = student_ranking()

        print("\n========== STUDENT RANKING ==========\n")

        if len(students) == 0:

            print("No Students Found.")

        else:

            print(
                f"{'RANK':<6}"
                f"{'NAME':<20}"
                f"{'MARKS':<10}"
                f"{'GRADE'}"
            )

            print("-" * 50)

            rank = 1

            for student in students:

                print(
                    f"{rank:<6}"
                    f"{student[1]:<20}"
                    f"{student[4]:<10}"
                    f"{student[5]}"
                )

                rank += 1

        log_info("Viewed Student Ranking")

        pause()


    # ===================================================
    # BACKUP DATABASE
    # ===================================================

    elif choice == "11":

        backup_database()

        log_info("Database Backup Created")

        pause()


    # ===================================================
    # RESTORE DATABASE
    # ===================================================

    elif choice == "12":

        restore_database()

        log_info("Database Restored")

        pause()


    # ===================================================
    # EXIT
    # ===================================================

    elif choice == "13":

        log_info("Application Closed")

        print("\n👋 Thank You for using Smart Student Management System!")

        break


    # ===================================================
    # INVALID CHOICE
    # ===================================================

    else:

        print("\n❌ Invalid Choice!")

        pause()