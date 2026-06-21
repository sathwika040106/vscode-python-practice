import os

file_name = "delete_me.txt"

if os.path.exists(file_name):
    os.remove(file_name)
    print("File Deleted Successfully")
else:
    print("File Not Found")