import re

phone = "9876543210"

pattern = r'^[6-9]\d{9}$'

if re.match(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")