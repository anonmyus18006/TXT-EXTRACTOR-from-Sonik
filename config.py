import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22215080"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "6ab80ad5d78fee18fdd9b909edfbafd5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "7841292070"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7841292070").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://sonickuwal_db_user:alfsMN6kIAt9qNQ1@cluster0.lqwg2ve.mongodb.net/?appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002355909549"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002355909549")  # Optional here you'll get all logs
