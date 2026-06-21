import random
import smtplib
import smtplib

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("YOUR_EMAIL", "YOUR_APP_PASSWORD")
        print("Login Successful")

except Exception as e:
    print(e)