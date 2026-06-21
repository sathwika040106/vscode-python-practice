from tkinter import *

root = Tk()

root.title("Label Demo")
root.geometry("400x300")

label = Label(
    root,
    text="Welcome Sathwika!",
    font=("Arial", 16)
)

label.pack(pady=20)

root.mainloop()