file = open("sample.txt", "r")

content = file.read()

words = content.split()

print("Word Count =", len(words))

file.close()