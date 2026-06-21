import os

while True:
    print("\nFILE MANAGER")
    print("1. View Files")
    print("2. Create Folder")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        files = os.listdir()

        for file in files:
            print(file)

    elif choice == "2":
        folder = input("Enter Folder Name: ")

        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Folder Created")
        else:
            print("Folder Already Exists")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")