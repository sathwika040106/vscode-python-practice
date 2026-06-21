import json

student = {
    "name": "Sathwika",
    "age": 21
}

result = json.dumps(student)

print(result)
print(type(result))