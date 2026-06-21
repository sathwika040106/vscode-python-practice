from datetime import date

date1 = date(2025, 1, 1)
date2 = date(2025, 12, 31)

difference = date2 - date1

print("Days:", difference.days)