from pyrogram import Client
from data import api_id, api_hash


with Client("account", api_id, api_hash) as app:
    app.send_message("79199496625", "Greetings from **Pyrogram** !")
