import customtkinter as ctk
from tkinter import messagebox
import sqlite3
import hashlib
import os

# ---------------- Appearance ----------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Database ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "students.db")


# ---------------- Login Function ----------------

def login():

    username = username_entry.get().strip()
    password = password_entry.get()

    password = hashlib.sha256(password.encode()).hexdigest()

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM admin
        WHERE username=?
        AND password=?
        """,
        (username, password)
    )

    admin = cursor.fetchone()

    connection.close()

    if admin:

        messagebox.showinfo(
            "Success",
            "Login Successful!"
        )

        window.destroy()

        import gui
        gui.start_gui()

    else:

        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password!"
        )


# ---------------- Window ----------------

window = ctk.CTk()

window.title("Smart Student Management")

window.geometry("500x500")

window.resizable(False, False)

# ---------------- Heading ----------------

title = ctk.CTkLabel(
    window,
    text="🎓 Smart Student Management",
    font=("Arial", 26, "bold")
)

title.pack(pady=40)

# ---------------- Username ----------------

username_entry = ctk.CTkEntry(
    window,
    width=300,
    placeholder_text="Username"
)

username_entry.pack(pady=15)

# ---------------- Password ----------------

password_entry = ctk.CTkEntry(
    window,
    width=300,
    placeholder_text="Password",
    show="*"
)

password_entry.pack(pady=15)

# ---------------- Login Button ----------------

login_btn = ctk.CTkButton(
    window,
    text="Login",
    width=300,
    height=40,
    command=login
)

login_btn.pack(pady=30)

# ---------------- Footer ----------------

footer = ctk.CTkLabel(
    window,
    text="Developed by Sathwika",
    font=("Arial", 12)
)

footer.pack(side="bottom", pady=20)

window.mainloop()