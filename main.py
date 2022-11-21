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

"""
1. Обработка текста
2. Обработка стикеров
3. Перенос всех обработчиков в плагины
4. Более реалистичная отправка сообщений
"""

# app = Client("account", config_file="config.ini")
app = Client("account", plugins=dict(root="plugins"))
# app = Client("account", api_id, api_hash)
group = 'mypythonlink'


with app:
    app.send_message("79199496625", "Greetings from **Pyrogram** !")




app.run()