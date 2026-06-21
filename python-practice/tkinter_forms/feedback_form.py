from tkinter import *

def submit():
    print(feedback.get("1.0", END))

root = Tk()
root.title("Feedback Form")
root.geometry("400x300")

Label(root, text="Feedback").pack()

feedback = Text(root, height=5, width=30)
feedback.pack()

Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()