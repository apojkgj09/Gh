import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import app
from YukkiMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(filters.regex("^كبرياء$") & filters.group)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5820455440)
    name = usr.first_name
    user = await client.get_chat(5820455440)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5820455440, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - [{usr.first_name}](https://t.me/FH_KN) ⚡
                        
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @FH_KN ⚡
                           
ႦᎥ᥆ | - {Bio} 🕷           
                          
Ꭵժ | - 5820455440 ⚡""", 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/FH_KN")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    zoharyus = "@FH_KN"
                    message_link = await Telegram.get_linok(message)
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(5820455440, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                           return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",)
