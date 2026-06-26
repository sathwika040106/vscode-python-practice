import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]

marks = [85, 90, 78, 95]

plt.bar(students, marks)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.show()