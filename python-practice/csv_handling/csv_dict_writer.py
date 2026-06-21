import csv

with open("employees.csv", "w", newline="") as file:
    fields = ["Name", "Salary"]

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    writer.writerow({
        "Name": "Sathwika",
        "Salary": 50000
    })

print("Employee data saved")