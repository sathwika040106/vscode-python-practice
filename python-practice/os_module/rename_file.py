import os

old_name = input("Enter old file name: ")
new_name = input("Enter new file name: ")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully")
else:
    print("File not found")