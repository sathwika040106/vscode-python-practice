import json

student = {
    "name": "Sathwika",
    "age": 21
}

with open("student.json", "w") as file:
    json.dump(student, file)

print("JSON file created")