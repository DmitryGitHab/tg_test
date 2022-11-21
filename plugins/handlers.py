from pyrogram import Client, filters

# @Client.on_message()
# def echo(client, message):
#     print("handlers")

@Client.on_message(filters.text)
async def text_handler(client, message):
    print(f"Пользователь отправил текст: {message.text}")
    print(f"Отвечаем пользователю..")
    await message.reply('Добрый вечер')

@Client.on_message(filters.sticker)
async def sticker_handler(client, message):
    print(f"Пользователь отправил стикер: {message.text}")
    print(f"Отвечаем пользователю..")
    await message.reply('Добрый вечер')