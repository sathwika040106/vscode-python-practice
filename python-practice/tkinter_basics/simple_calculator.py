from tkinter import *

def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result.config(text=f"Result: {num1 + num2}")

root = Tk()

root.title("Simple Calculator")
root.geometry("400x300")

Label(root, text="Number 1").pack()

entry1 = Entry(root)
entry1.pack()

Label(root, text="Number 2").pack()

entry2 = Entry(root)
entry2.pack()

Button(
    root,
    text="Add",
    command=add
).pack(pady=10)

result = Label(root, text="")
result.pack()

root.mainloop()