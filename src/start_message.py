from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/4d0bc819e4b30f7207e04.jpg"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

Welcome to Anime DL Bot, Here you can Download all Anime for FREE 😁 ,For TG Anime Join @Anime_Collectors 
!!!

Please read all the instructions about the bot before surfing on...

See /whats_new to know about latest updates...""", reply_markup=reply_markup)
