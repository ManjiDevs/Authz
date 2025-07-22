import requests
import sys
from telegram import Bot
import asyncio

API_URL = "https://creativedemon.pythonanywhere.com/verify"
SCRIPT_ID = "autobot_v1"

def id(custom_id):
    asyncio.run(authenticate(custom_id))

async def authenticate(custom_id):
    try:
        print("🔐 Validating license...")

        bot = Bot(token=sys.argv[1])
        bot_info = await bot.get_me()

        payload = {
            "custom_id": custom_id,
            "script_id": SCRIPT_ID,
            "bot_token": sys.argv[1],
            "bot_username": bot_info.username,
        }

        response = requests.post(API_URL, json=payload)
        data = response.json()

        if not data.get("authorized"):
            print("❌ Unauthorized script usage.")
            sys.exit()

        print(f"✅ Hello @{bot_info.username} — Access Granted ✅")

    except Exception as e:
        print("❌ License check failed:", e)
        sys.exit()
