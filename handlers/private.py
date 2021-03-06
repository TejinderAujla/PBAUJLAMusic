import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
     await message.reply_photo(
        photo=f"https://te.legra.ph/file/bb99dc371aae5deb5ec8d.jpg",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ ๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ ๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ = [เผ๏ธโโขไบใTejinder Aujlaใไบโขโ ](https://t.me/Aujla_PB_65)
        
        
๐๐ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐๐ง๐ฒ ๐๐ฎ๐๐ฌ๐ญ๐ข๐จ๐ง๐ฌ ๐๐ง๐ ๐๐๐ฅ๐ฉ ๐๐ก๐๐ง ๐๐ฆ ๐๐ฒ ๐๐จ๐ฌ๐ฌ = [เผ๏ธโโขไบใTejinder Aujlaใไบโขโ ](https://t.me/Aujla_PB_65)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("โ Add me to your Group", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("๐ค ๐๐ซ๐๐๐ญ๐จ๐ซ", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("โ๏ธ ๐๐จ๐ฎ๐ซ๐๐ ", url=f"https://github.com/TejinderAujla/PBAUJLAMusic")
                ],[
                    InlineKeyboardButton("๐จ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ ", url=f"https://t.me/Lions_OF_Punjab"),
                    InlineKeyboardButton("๐จ ๐๐ฉ๐๐๐ญ๐", url=f"https://t.me/AujlaPB65_Network")
                ],[
                    InlineKeyboardButton("๐ How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**ร I am Alive ร**\n\n@Lions_OF_Punjab ๐ก")


@Client.on_message(command(["repo"]) & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("`Click on the Button given below to Get the Bot Source Code.`",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ๏ธ ๐๐จ๐ฎ๐ซ๐๐ ", url=f"https://github.com/TejinderAujla/PBAUJLAMusic")
                ]
            ]
        ),
    )
