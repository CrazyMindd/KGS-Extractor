import os

api_id = 28228907
api_hash = os.environ.get("API_HASH", "3848da16c807890cabc8d1395248c9cf3")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "6127558921")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6127558921")
owner_users = [int(num) for num in osowner_users.split(",")]
