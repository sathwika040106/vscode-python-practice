import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "students.csv")

df = pd.read_csv(csv_path)

print(df.columns.tolist())

high_scores = df[df["Marks"] > 85]

print(high_scores)