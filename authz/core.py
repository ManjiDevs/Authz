import requests

API_URL = "https://creativedemon.pythonanywhere.com"

def id(custom_id: str, bot_token: str = "", bot_username: str = "") -> bool:
    """Check if a bot is authorized."""
    payload = {
        "custom_id": custom_id,
        "bot_token": bot_token,
        "bot_username": bot_username,
    }
    try:
        res = requests.post(f"{API_URL}/verify", json=payload, timeout=10)
        return res.status_code == 200 and res.json().get("authorized") is True
    except Exception:
        return False