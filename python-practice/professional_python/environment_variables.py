from dotenv import load_dotenv
import os

load_dotenv()

print("API Key:", os.getenv("API_KEY"))

print("App Name:", os.getenv("APP_NAME"))