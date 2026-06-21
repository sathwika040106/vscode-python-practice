from tkinter import *

def submit():
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())

root = Tk()
root.title("Registration Form")
root.geometry("400x300")

Label(root, text="Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Email").pack()
email_entry = Entry(root)
email_entry.pack()

Button(root, text="Register", command=submit).pack(pady=10)

root.mainloop()