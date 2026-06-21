from tkinter import *

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        result.config(text="Login Successful")
    else:
        result.config(text="Login Failed")

root = Tk()
root.title("Login Form")
root.geometry("400x300")

Label(root, text="Username").pack()
user_entry = Entry(root)
user_entry.pack()

Label(root, text="Password").pack()
pass_entry = Entry(root, show="*")
pass_entry.pack()

Button(root, text="Login", command=login).pack(pady=10)

result = Label(root, text="")
result.pack()

root.mainloop()