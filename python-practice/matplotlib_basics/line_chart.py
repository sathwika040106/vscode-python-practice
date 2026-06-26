import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 250, 300, 280, 350]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.grid(True)

plt.show()