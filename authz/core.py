import requests

class Authz:
    def __init__(self, api_url="https://creativedemon.pythonanywhere.com/verify"):
        self.api_url = api_url

    def verify(self, custom_id: str, bot_token: str, bot_username: str) -> bool:
        try:
            res = requests.post(self.api_url, json={
                "custom_id": custom_id,
                "bot_token": bot_token,
                "bot_username": bot_username
            })
            return res.json().get("authorized", False)
        except Exception as e:
            print(f"[Authz] Error: {e}")
            return False
