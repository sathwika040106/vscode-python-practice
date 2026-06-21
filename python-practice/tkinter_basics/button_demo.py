from tkinter import *

def show_message():
    print("Button Clicked")

root = Tk()

root.title("Button Demo")
root.geometry("400x300")

btn = Button(
    root,
    text="Click Me",
    command=show_message
)

btn.pack(pady=20)

root.mainloop()