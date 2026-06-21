import os

folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder Created Successfully")
else:
    print("Folder Already Exists")