from pyrogram import Client

@Client.on_message()
def echo(client, message):
    print("handlers")