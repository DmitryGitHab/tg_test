from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from pyrogram import Client, filters, StopPropagation
from data import api_id, api_hash, app_version, device_model, system_version, lang_code
from pyrogram.handlers import MessageHandler
import configparser
import plugins
import time
from time import sleep
import random

# with Client("account", api_id, api_hash) as app:
#     app.send_message("79199496625", "Greetings from **Pyrogram** !")

# app = Client("account", config_file="config.ini")
app = Client("account", plugins=dict(root="plugins"))
# app = Client("account", api_id, api_hash)
group = 'mypythonlink'


with app:
    app.send_message("79199496625", "Greetings from **Pyrogram** !",)


# async def main():
#     async with app:
#         await app.send_message("79199496625", "Greetings from **Pyrogram** NEW!")
#
# @app.on_message()
# async def my_handler(client, message):
#     await message.forward("me")

"""
def my_function(client, message):
    message.forward("me")

my_handler = MessageHandler(my_function)
app.add_handler(my_handler)
app.run()
"""

#
# with Client("account", api_id, api_hash) as app:
#     app.send_message(group, "Greetings from **Pyrogram** !")

"""
@app.on_message()
def echo(client, message):
    print(message)
    app.send_message(message.chat.id, "test")
app.run()
"""


# with app:
#     with open('file', 'rb') as file:
#         app.send_document('me', file)

"""
@app.on_message(filters.text)
def echo(client, message):
    app.send_message(message.chat.id, message.text)
    with open('file', 'rb') as file:
        app.send_document(message.chat.id, 'file')

app.run()
"""



"""
def func(_, __, query):
    return not query.from_user.is_bot

static_data_filter =filters.create(func)

"""

"""
# static_data_filter = filters.create(lambda _, __, query: not query.from_user.is_bot)

@app.on_message(static_data_filter)
def pyrogram_data(client, message):
    message.forward(group)
"""

""" фильтрация если не бот"""

"""
def func(_, __, query):
    return not query.from_user.is_bot

static_data_filter = filters.create(func)


# static_data_filter = filters.create(lambda _, __, query: not query.from_user.is_bot)

@app.on_message(static_data_filter)
def pyrogram_data(client, message):
    # message.forward(group)
    print(message.text)
"""

# app.run()

# @app.on_message()
# def echo(client, message):
#     print(message)
#     app.send_message(message.chat.id, "test")
#
#
# app.run()






""" планирование задач"""

"""
# async def job():
#     await app.send_message("me", f"{int(time.time())}")


def job():
    app.send_message("me", f"{(time.time())}")

# scheduler = AsyncIOScheduler()
scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=3)

scheduler.start()
app.run()
"""

""" Группы фильтров"""
""" 
@app.on_message(filters.text | filters.sticker)
def text_or_sticker(client, message):
    print("Text or sticker")
    raise StopPropagation
    # raise StopPropagation


@app.on_message(filters.text, group=1)
def just_text(client, message):
    print("just_text")
"""

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


app.run()