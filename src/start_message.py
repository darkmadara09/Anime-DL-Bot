from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/4d0bc819e4b30f7207e04.jpg"
    message.reply_photo(pic_url, caption=f"""<b>Hi {message.chat.first_name}</b>,

Welcome to Anime DL Bot

<em>Please read all the instructions about the bot before surfing on...</em>

See /whats_new to know about latest updates...""", reply_markup=reply_markup, parse_mode="html")
