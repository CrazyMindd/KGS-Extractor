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

import helpers.vid as helper
from CrazyMind.CrazyConfig import *
from helpers.button import keyboard
from helpers.sudoers import *
from helpers.text import *

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
            "✨ Hello Sir,\n\nYou Don't Have Right To Access This Contact Owner:- @Crazy_Mind_Official",
        )
    await m.reply_text("➭ 𝗕𝗼𝘁 𝗜𝘀 𝗕𝗲𝗶𝗻𝗴 𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴. 𝗣𝗹𝗲𝗮𝘀𝗲 𝗞𝗲𝗲𝗽 𝗣𝗮𝘁𝗶𝗲𝗻𝗰𝗲", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["khan"]))
async def khan_login(app, message):
    input1 = await app.ask(message.chat.id, text="**Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password**")

    login_url = "https://khanglobalstudies.com/api/login-with-password"
    raw_text = input1.text

    headers = {
        "Host": "khanglobalstudies.com",
        "content-type": "application/x-www-form-urlencoded",
        "content-length": "36",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    data = {
        "password": "",
        "phone": ""
    }
    data["phone"] = raw_text.split("*")[0]
    data["password"] = raw_text.split("*")[1]
    await input1.delete(True)

    response = requests.post(login_url, headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()
        token = data["token"]
        await message.reply_text("**Login Successful**")
    else:
        await message.reply_text("Go back to response")

    headers = {
        "Host": "khanglobalstudies.com",
        "authorization": f"Bearer {token}",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    course_url = "https://khanglobalstudies.com/api/user/v2/courses"
    response = requests.get(course_url, headers=headers)

    data = response.json()
    courses = [(course['id'], course['title']) for course in data]

    FFF = "BATCH-ID  - BATCH-NAME\n\n"

    for course_id, course_title in courses:
        FFF += f"`{course_id}` - **{course_title}**\n\n"

    await message.reply_text(FFF)

    input3 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")    
    raw_text3 = input3.text
    for course in data:
        if course['id'] == raw_text3:
            batch_name = course['title']
        else:
            batch_name = "KHAN-SIR"
    url = "https://khanglobalstudies.com/api/user/courses/"+raw_text3+"/v2-lessons"
    response2 = requests.get(url, headers=headers)
    
    msg = await message.reply_text("**Prepared your course id**")
    bat_id = ""
    for data in response2.json():
        baid = f"{data['id']}&"
        bat_id += baid
          
    await msg.edit_text("**Done your course id\n Now Extracting your course**")
    full = ""
    try:
        xv = bat_id.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
            try:
                url = "https://khanglobalstudies.com/api/lessons/"+t  
                response = requests.get(url, headers=headers)
                data = response.json()
                
        
                videos = data.get('videos', [])
                fuck = ""
                for video in videos: 
                    class_title = video.get('name')
                    class_url = video.get('video_url')
                    fuck += f"{class_title}: {class_url}\n"
        
                full += fuck
            except Exception as e:
                print(str(e))
                pass
                
        with open(f"{batch_name}.txt", 'a') as f:
            f.write(f"{full}")
        
        c_txt = f"**https://envs.sh/082.jpg\nApp Name: Khan Global Studies (KGS)\nBatch Name:** `{batch_name}`"
        await message.reply_document(document=f"{batch_name}.txt", caption=c_txt)
        os.remove(f"{batch_name}.txt")

    except Exception as e:
        await message.reply_text(str(e))



