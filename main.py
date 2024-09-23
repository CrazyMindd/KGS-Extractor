import asyncio
import json
import logging
import os
import re
import subprocess
import sys
import time
from logging.handlers import RotatingFileHandler
from subprocess import getstatusoutput

import requests
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from pyromod import listen

import online.helpers.vid as helper
from online.Config import *
from online.helpers.button import keyboard
from online.helpers.sudoers import *
from online.helpers.text import *

from utils import get_datetime_str, create_html_file
# ==========Logging==========#
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging = logging.getLogger()

# =========== Client ===========#
bot = Client(
    "bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
)

print(listen.__file__)



# ============== Start Commands ==========#
@bot.on_message(filters.command(["start"]))
async def account_lstarn(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_photo(
            photo="https://graph.org/file/9d91fcf92474618cf49ae.jpg",
            caption=paid_text,
            reply_markup=keyboard,
        )
    await m.reply_text(start_text)


# ========== Global Concel Command ============
cancel = False


@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    if not two(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\nThis Command is only For Owner",
            reply_markup=keyboard,
        )
    editable = await m.reply_text(
        "Canceling All process Plz wait\n🚦🚦 Last Process Stopped 🚦🚦"
    )
    global cancel
    cancel = False
    await editable.edit("cancelled all")
    return


# ============== Power Commands =================
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    if not two(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\nYou Don't Have Right To Access This Contact Owner",
        )
    await m.reply_text("➭ 𝗕𝗼𝘁 𝗜𝘀 𝗕𝗲𝗶𝗻𝗴 𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴. 𝗣𝗹𝗲𝗮𝘀𝗲 𝗞𝗲𝗲𝗽 𝗣𝗮𝘁𝗶𝗲𝗻𝗰𝗲", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
