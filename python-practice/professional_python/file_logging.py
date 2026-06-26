import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program Started")

logging.warning("Low Memory")

logging.error("Database Error")

print("Logs Saved")