import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Name:", row["Name"])
        print("Salary:", row["Salary"])