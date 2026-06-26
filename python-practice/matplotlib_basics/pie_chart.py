import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "SQL"]

hours = [8, 5, 3, 4]

plt.pie(hours, labels=subjects, autopct="%1.1f%%")

plt.title("Study Time Distribution")

plt.show()