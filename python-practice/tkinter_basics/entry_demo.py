from tkinter import *

def display_name():
    print(entry.get())

root = Tk()

root.title("Entry Demo")
root.geometry("400x300")

entry = Entry(root, width=30)
entry.pack(pady=10)

btn = Button(
    root,
    text="Submit",
    command=display_name
)

btn.pack()

root.mainloop()