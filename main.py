from pyrogram import Client
from data import api_id, api_hash
from pyrogram.handlers import MessageHandler

# with Client("account", api_id, api_hash) as app:
#     app.send_message("79199496625", "Greetings from **Pyrogram** !")


app = Client("account", api_id, api_hash)


# async def main():
#     async with app:
#         await app.send_message("79199496625", "Greetings from **Pyrogram** NEW!")
#
# @app.on_message()
# async def my_handler(client, message):
#     await message.forward("me")

def my_function(client, message):
    message.forward("me")

my_handler = MessageHandler(my_function)
app.add_handler(my_handler)
app.run()