import os

api_id = 28528007
api_hash = os.environ.get("API_HASH", "38464da16c80310cabc8d13952419cf3")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6329158981")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6329158981")
owner_users = [int(num) for num in osowner_users.split(",")]
