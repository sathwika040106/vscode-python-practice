import re

text = "My age is 21 and my score is 95"

numbers = re.findall(r'\d+', text)

print(numbers)