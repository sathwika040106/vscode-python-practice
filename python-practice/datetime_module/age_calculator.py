from datetime import date

birth_year = int(input("Enter Birth Year: "))

current_year = date.today().year

age = current_year - birth_year

print("Your Age:", age)