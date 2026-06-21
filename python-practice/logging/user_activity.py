import logging

logging.basicConfig(
    filename="user_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

username = input("Enter Username: ")

logging.info(f"{username} logged in")

print("Activity Recorded")