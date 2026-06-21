import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "students.csv")

df = pd.read_csv(csv_path)

print(df.columns.tolist())

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())