import matplotlib.pyplot as plt

marks = [70, 75, 80, 82, 85, 90, 95, 88, 91, 77]

plt.hist(marks, bins=5)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()