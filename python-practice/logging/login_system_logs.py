import logging

logging.basicConfig(
    filename="login.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

username = input("Username: ")
password = input("Password: ")

if password == "admin123":
    print("Login Successful")
    logging.info(f"{username} Login Successful")
else:
    print("Login Failed")
    logging.warning(f"{username} Login Failed")