import json

data = '{"name": "Sathwika", "age": 21}'

result = json.loads(data)

print(result)
print(type(result))