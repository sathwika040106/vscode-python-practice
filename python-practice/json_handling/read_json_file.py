import json

try:
    with open("json_handling/student.json", "r") as file:
        data = json.load(file)

    print("Name :", data["name"])
    print("Course :", data["course"])
    print("Marks :", data["marks"])

except FileNotFoundError:
    print("student.json file not found")

except json.JSONDecodeError:
    print("Invalid JSON format")