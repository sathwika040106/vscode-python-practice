from tkinter import *

def register():
    output.config(
        text=f"Name: {name_entry.get()}\nCourse: {course_entry.get()}"
    )

root = Tk()
root.title("Student Registration")
root.geometry("400x350")

Label(root, text="Student Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Course").pack()
course_entry = Entry(root)
course_entry.pack()

Button(
    root,
    text="Register",
    command=register
).pack(pady=10)

output = Label(root, text="")
output.pack()

root.mainloop()