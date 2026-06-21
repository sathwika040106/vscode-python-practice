from tkinter import *

def save():
    print("Student:", name_entry.get())
    print("Marks:", marks_entry.get())

root = Tk()
root.title("Student Form")
root.geometry("400x300")

Label(root, text="Student Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Marks").pack()
marks_entry = Entry(root)
marks_entry.pack()

Button(root, text="Save", command=save).pack(pady=10)

root.mainloop()