import re

text = "Python is easy to learn"

result = re.search("easy", text)

if result:
    print("Word Found")
else:
    print("Word Not Found")