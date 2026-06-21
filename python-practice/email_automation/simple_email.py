from email.message import EmailMessage

email = EmailMessage()

email["Subject"] = "Test"
email["From"] = "abc@gmail.com"
email["To"] = "xyz@gmail.com"

email.set_content("Hello")

print(email)