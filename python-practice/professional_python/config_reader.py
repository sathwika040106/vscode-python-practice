import json

config = {
    "app_name": "Student Manager",
    "version": "1.0"
}

with open("config.json", "w") as file:
    json.dump(config, file)

with open("config.json", "r") as file:
    data = json.load(file)

print(data)