import smtplib

email = input("Enter Gmail: ")
app_password = input("Enter App Password: ")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, app_password)
        print("Login Successful")
except Exception as e:
    print("Error:", e)