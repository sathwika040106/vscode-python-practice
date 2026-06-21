import json

student = {
    "name": "Sathwika",
    "course": "Python",
    "marks": 95
}

json_data = json.dumps(student, indent=4)

print(json_data)