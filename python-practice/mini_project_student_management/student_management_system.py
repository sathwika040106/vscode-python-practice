def add_student():
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")

    print("Student Added Successfully")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

        if not data:
            print("No Records Found")
            return

        print("\nStudent Records")
        print("----------------")

        for student in data:
            name, marks = student.strip().split(",")
            print(f"Name: {name} | Marks: {marks}")

    except FileNotFoundError:
        print("No Student Records Found")


def search_student():
    search_name = input("Enter Student Name: ")

    try:
        with open("students.txt", "r") as file:
            found = False

            for student in file:
                name, marks = student.strip().split(",")

                if name.lower() == search_name.lower():
                    print(f"Found -> {name} : {marks}")
                    found = True

            if not found:
                print("Student Not Found")

    except FileNotFoundError:
        print("No Records Found")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")