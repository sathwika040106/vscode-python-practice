from datetime import date

birth_month = int(input("Enter Birth Month: "))
birth_day = int(input("Enter Birth Day: "))

today = date.today()

birthday = date(today.year, birth_month, birth_day)

if birthday < today:
    birthday = date(today.year + 1, birth_month, birth_day)

days_left = (birthday - today).days

print("Days until your birthday:", days_left)