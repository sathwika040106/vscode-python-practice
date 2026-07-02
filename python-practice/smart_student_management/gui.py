import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
import pandas as pd
import shutil
import datetime
import os

from database import *
from student import Student
from validations import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class StudentManagementGUI:

    def __init__(self):

        self.app = ctk.CTk()

        self.app.title("Smart Student Management System")

        self.app.geometry("1200x700")

        self.app.resizable(False, False)

        self.create_layout()

        self.show_dashboard()

    # =========================

    def create_layout(self):

        self.sidebar = ctk.CTkFrame(
            self.app,
            width=230,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content = ctk.CTkFrame(self.app)

        self.content.pack(
            side="right",
            expand=True,
            fill="both"
        )

        self.build_sidebar()

    # =========================

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    # =========================

    def build_sidebar(self):

        ctk.CTkLabel(

            self.sidebar,

            text="🎓\nSmart Student\nManagement",

            font=("Arial",22,"bold")

        ).pack(pady=20)

        buttons = [

            ("🏠 Dashboard", self.show_dashboard),

            ("➕ Add Student", self.add_student_window),

            ("👀 View Students", self.view_students_window),

            ("🔍 Search Student", self.search_student_window),

            ("✏ Update Student", self.update_student_window),

            ("❌ Delete Student", self.delete_student_window),

            ("🏆 Student Ranking", self.student_ranking_window),

            ("📈 Graph Analytics", self.graph_window),

            ("📄 PDF Report", self.generate_pdf),

            ("📁 Export CSV", self.export_csv),

            ("💾 Backup", self.backup_database),

            ("♻ Restore", self.restore_database),

            ("🌙 Theme", self.toggle_theme),

            ("🚪 Exit", self.app.destroy)

        ]

        for text, command in buttons:

            ctk.CTkButton(

                self.sidebar,

                text=text,

                width=200,

                command=command

            ).pack(pady=6)

    # =========================

    def create_card(self,parent,title,value):

        frame = ctk.CTkFrame(

            parent,

            width=180,

            height=120

        )

        frame.pack(side="left",padx=15)

        frame.pack_propagate(False)

        ctk.CTkLabel(

            frame,

            text=title,

            font=("Arial",18)

        ).pack(pady=10)

        ctk.CTkLabel(

            frame,

            text=value,

            font=("Arial",30,"bold")

        ).pack()

    # =========================

    def show_dashboard(self):

        self.clear_content()

        ctk.CTkLabel(

            self.content,

            text="Welcome Admin 👋",

            font=("Arial",30,"bold")

        ).pack(pady=30)

        cards = ctk.CTkFrame(self.content)

        cards.pack(pady=30)

        data = get_dashboard_data()

        self.create_card(cards,"Students",str(data["total"]))

        self.create_card(cards,"Average",str(data["average"]))

        self.create_card(cards,"Highest",str(data["highest"]))

        self.create_card(cards,"Lowest",str(data["lowest"]))

    # =========================

    def toggle_theme(self):

        if ctk.get_appearance_mode()=="Dark":

            ctk.set_appearance_mode("light")

        else:

            ctk.set_appearance_mode("dark")

    # =========================
        # =========================
    # ADD STUDENT
    # =========================

    def add_student_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="➕ Add Student",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        frame = ctk.CTkFrame(self.content)
        frame.pack(pady=20)

        name = ctk.CTkEntry(frame, width=350, placeholder_text="Student Name")
        name.pack(pady=8)

        age = ctk.CTkEntry(frame, width=350, placeholder_text="Age")
        age.pack(pady=8)

        email = ctk.CTkEntry(frame, width=350, placeholder_text="Email")
        email.pack(pady=8)

        marks = ctk.CTkEntry(frame, width=350, placeholder_text="Marks")
        marks.pack(pady=8)

        def save():
            print("Save button clicked")

            n = name.get().strip()
            a = age.get().strip()
            e = email.get().strip()
            m = marks.get().strip()
            print(n, a, e, m)


            grade = calculate_grade(int(m))

            student = Student(
                n,
                int(a),
                e,
                int(m),
                grade
            )
            print(student)

            add_student(student)
            print("Student added successfully")


            messagebox.showinfo(
                "Success",
                "Student Added Successfully!"
            )

            name.delete(0, "end")
            age.delete(0, "end")
            email.delete(0, "end")
            marks.delete(0, "end")

        ctk.CTkButton(
            frame,
            text="Save Student",
            command=save
        ).pack(pady=20)

    # =========================
    # VIEW STUDENTS
    # =========================

    def view_students_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="👀 View Students",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        columns = (
            "ID",
            "Name",
            "Age",
            "Email",
            "Marks",
            "Grade"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings",
            height=18
        )

        for col in columns:

            tree.heading(col, text=col)

            tree.column(
                col,
                width=140,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            self.content,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        students = get_all_students()

        for student in students:

            tree.insert(
                "",
                "end",
                values=student
            )

        def show_profile(event):

            item = tree.focus()

            if not item:
                return

            values = tree.item(item)["values"]

            win = ctk.CTkToplevel(self.app)

            win.title("Student Profile")

            win.geometry("400x400")

            labels = [

                f"ID : {values[0]}",
                f"Name : {values[1]}",
                f"Age : {values[2]}",
                f"Email : {values[3]}",
                f"Marks : {values[4]}",
                f"Grade : {values[5]}"

            ]

            ctk.CTkLabel(
                win,
                text="👤 Student Profile",
                font=("Arial", 24, "bold")
            ).pack(pady=20)

            for txt in labels:

                ctk.CTkLabel(
                    win,
                    text=txt,
                    font=("Arial", 18)
                ).pack(pady=5)

        tree.bind("<Double-1>", show_profile)
            # =========================
    # SEARCH STUDENT
    # =========================

    def search_student_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="🔍 Search Student",
            font=("Arial",28,"bold")
        ).pack(pady=20)

        search_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="Enter Student Name"
        )

        search_entry.pack(pady=10)

        columns = (
            "ID",
            "Name",
            "Age",
            "Email",
            "Marks",
            "Grade"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:

            tree.heading(col,text=col)

            tree.column(col,width=130,anchor="center")

        tree.pack(fill="x",padx=20,pady=20)

        def search_now():

            tree.delete(*tree.get_children())

            keyword = search_entry.get().strip()

            students = search_student(keyword)

            if not students:

                messagebox.showinfo(
                    "Search",
                    "No Student Found"
                )

                return

            for student in students:

                tree.insert(
                    "",
                    "end",
                    values=student
                )

        ctk.CTkButton(
            self.content,
            text="Search",
            command=search_now
        ).pack()

    # =========================
    # UPDATE STUDENT
    # =========================

    def update_student_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="✏ Update Student",
            font=("Arial",28,"bold")
        ).pack(pady=20)

        id_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="Student ID"
        )
        id_entry.pack(pady=8)

        name_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="New Name"
        )
        name_entry.pack(pady=8)

        age_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="New Age"
        )
        age_entry.pack(pady=8)

        email_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="New Email"
        )
        email_entry.pack(pady=8)

        marks_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="New Marks"
        )
        marks_entry.pack(pady=8)

        def update_now():

            try:

                student_id = int(id_entry.get())

            except:

                messagebox.showerror(
                    "Error",
                    "Invalid Student ID"
                )

                return

            name = name_entry.get().strip()

            age = age_entry.get().strip()

            email = email_entry.get().strip()

            marks = marks_entry.get().strip()

            if not validate_name(name):

                messagebox.showerror("Error","Invalid Name")
                return

            if not validate_age(age):

                messagebox.showerror("Error","Invalid Age")
                return

            if not validate_email(email):

                messagebox.showerror("Error","Invalid Email")
                return

            if not validate_marks(marks):

                messagebox.showerror("Error","Invalid Marks")
                return

            grade = calculate_grade(int(marks))

            student = Student(
                name,
                int(age),
                email,
                int(marks),
                grade
            )

            update_student(student_id,student)

            messagebox.showinfo(
                "Success",
                "Student Updated Successfully!"
            )

        ctk.CTkButton(
            self.content,
            text="Update Student",
            command=update_now
        ).pack(pady=20)

    # =========================
    # DELETE STUDENT
    # =========================

    def delete_student_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="❌ Delete Student",
            font=("Arial",28,"bold")
        ).pack(pady=30)

        id_entry = ctk.CTkEntry(
            self.content,
            width=350,
            placeholder_text="Student ID"
        )

        id_entry.pack(pady=15)

        def delete_now():

            try:

                student_id = int(id_entry.get())

            except:

                messagebox.showerror(
                    "Error",
                    "Invalid Student ID"
                )

                return

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Delete this student?"
            )

            if not confirm:

                return

            delete_student(student_id)

            messagebox.showinfo(
                "Success",
                "Student Deleted Successfully!"
            )

            id_entry.delete(0,"end")

        ctk.CTkButton(
            self.content,
            text="Delete Student",
            fg_color="red",
            hover_color="#990000",
            command=delete_now
        ).pack(pady=20)
            # =========================
    # STUDENT RANKING
    # =========================

    def student_ranking_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="🏆 Student Ranking",
            font=("Arial",28,"bold")
        ).pack(pady=20)

        columns = (
            "Rank",
            "ID",
            "Name",
            "Marks",
            "Grade"
        )

        tree = ttk.Treeview(
            self.content,
            columns=columns,
            show="headings",
            height=18
        )

        for col in columns:

            tree.heading(col,text=col)

            tree.column(
                col,
                width=120,
                anchor="center"
            )

        tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        students = get_student_ranking()

        medals = {

            1:"🥇",
            2:"🥈",
            3:"🥉"

        }

        rank = 1

        for student in students:

            medal = medals.get(rank,str(rank))

            tree.insert(
                "",
                "end",
                values=(
                    medal,
                    student[0],
                    student[1],
                    student[2],
                    student[3]
                )
            )

            rank += 1

    # =========================
    # GRAPH MENU
    # =========================

    def graph_window(self):

        self.clear_content()

        ctk.CTkLabel(
            self.content,
            text="📈 Graph Analytics",
            font=("Arial",28,"bold")
        ).pack(pady=20)

        ctk.CTkButton(
            self.content,
            text="📊 Bar Chart",
            width=250,
            command=self.bar_chart
        ).pack(pady=10)

        ctk.CTkButton(
            self.content,
            text="📈 Line Chart",
            width=250,
            command=self.line_chart
        ).pack(pady=10)

        ctk.CTkButton(
            self.content,
            text="🥧 Pie Chart",
            width=250,
            command=self.pie_chart
        ).pack(pady=10)

    # =========================
    # BAR CHART
    # =========================

    def bar_chart(self):

        data = get_marks_data()

        if not data:

            messagebox.showinfo(
                "Graph",
                "No Student Data Found"
            )

            return

        names = [x[0] for x in data]

        marks = [x[1] for x in data]

        plt.figure(figsize=(10,5))

        plt.bar(names,marks)

        plt.title("Student Marks")

        plt.xlabel("Students")

        plt.ylabel("Marks")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    # =========================
    # LINE CHART
    # =========================

    def line_chart(self):

        data = get_marks_data()

        if not data:

            messagebox.showinfo(
                "Graph",
                "No Student Data Found"
            )

            return

        names = [x[0] for x in data]

        marks = [x[1] for x in data]

        plt.figure(figsize=(10,5))

        plt.plot(
            names,
            marks,
            marker="o",
            linewidth=3
        )

        plt.title("Performance Trend")

        plt.xlabel("Students")

        plt.ylabel("Marks")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    # =========================
    # PIE CHART
    # =========================

    def pie_chart(self):

        data = get_marks_data()

        if not data:

            messagebox.showinfo(
                "Graph",
                "No Student Data Found"
            )

            return

        names = [x[0] for x in data]

        marks = [x[1] for x in data]

        plt.figure(figsize=(8,8))

        plt.pie(
            marks,
            labels=names,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Marks Distribution")

        plt.show()
            # =========================
    # PDF REPORT
    # =========================

    def generate_pdf(self):

        students = get_report_data()

        if not students:

            messagebox.showinfo(
                "PDF Report",
                "No Student Data Found"
            )
            return

        from reportlab.platypus import (
            SimpleDocTemplate,
            Table,
            TableStyle,
            Paragraph
        )

        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors

        pdf = SimpleDocTemplate("Student_Report.pdf")

        styles = getSampleStyleSheet()

        elements = []

        elements.append(

            Paragraph(
                "Smart Student Management System",
                styles["Title"]
            )

        )

        data = [[

            "ID",
            "Name",
            "Age",
            "Email",
            "Marks",
            "Grade"

        ]]

        for student in students:

            data.append(student)

        table = Table(data)

        table.setStyle(

            TableStyle([

                ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

                ("TEXTCOLOR",(0,0),(-1,0),colors.white),

                ("GRID",(0,0),(-1,-1),1,colors.black),

                ("BACKGROUND",(0,1),(-1,-1),colors.beige),

                ("ALIGN",(0,0),(-1,-1),"CENTER"),

                ("BOTTOMPADDING",(0,0),(-1,0),10)

            ])

        )

        elements.append(table)

        pdf.build(elements)

        messagebox.showinfo(

            "Success",

            "Student_Report.pdf Generated Successfully!"

        )

    # =========================
    # EXPORT CSV
    # =========================

    def export_csv(self):

        students = get_csv_data()

        if not students:

            messagebox.showinfo(
                "CSV Export",
                "No Student Data Found"
            )
            return

        df = pd.DataFrame(

            students,

            columns=[

                "ID",

                "Name",

                "Age",

                "Email",

                "Marks",

                "Grade"

            ]

        )

        file = filedialog.asksaveasfilename(

            defaultextension=".csv",

            filetypes=[

                ("CSV File","*.csv")

            ],

            initialfile="Student_Report.csv"

        )

        if not file:

            return

        df.to_csv(

            file,

            index=False

        )

        messagebox.showinfo(

            "Success",

            "CSV Export Successful!"

        )
            # =========================
    # BACKUP DATABASE
    # =========================

    def backup_database(self):

        db_path = "students.db"

        if not os.path.exists(db_path):

            messagebox.showerror(
                "Error",
                "Database not found!"
            )

            return

        backup_folder = "backup"

        os.makedirs(
            backup_folder,
            exist_ok=True
        )

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_file = os.path.join(
            backup_folder,
            f"students_backup_{timestamp}.db"
        )

        shutil.copy(
            db_path,
            backup_file
        )

        messagebox.showinfo(
            "Backup Successful",
            f"Backup saved to:\n{backup_file}"
        )

    # =========================
    # RESTORE DATABASE
    # =========================

    def restore_database(self):

        file = filedialog.askopenfilename(

            title="Select Backup File",

            filetypes=[

                ("Database File","*.db")

            ]

        )

        if not file:

            return

        confirm = messagebox.askyesno(

            "Restore",

            "Current database will be replaced.\nContinue?"

        )

        if not confirm:

            return

        shutil.copy(
            file,
            "students.db"
        )

        messagebox.showinfo(
            "Success",
            "Database Restored Successfully!"
        )

    # =========================
    # TOGGLE THEME
    # =========================

    def toggle_theme(self):

        current = ctk.get_appearance_mode()

        if current == "Dark":

            ctk.set_appearance_mode("light")

        else:

            ctk.set_appearance_mode("dark")

    # =========================
    # RUN APPLICATION
    # =========================

    def run(self):

        self.app.mainloop()


# =========================
# START GUI
# =========================

def start_gui():

    app = StudentManagementGUI()

    app.run()


if __name__ == "__main__":

    start_gui()