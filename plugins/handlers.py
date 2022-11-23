import asyncio
from pyrogram import Client, filters, enums


# @Client.on_message()
# def echo(client, message):
#     print("handlers")

async def message_handler(client_obj, message_obj, text):
    print("Получили сообщение, ожидаем 5с..")
    await asyncio.sleep(5)
    await client_obj.read_chat_history(message_obj.chat.id)
    print("Прочитали сообщение пользователя")
    print("имитируем ввод сообщения")

    await asyncio.sleep(3)
    # await client_obj.send_chat_action(message_obj.chat.id, "typing")
    await client_obj.send_chat_action(message_obj.chat.id, enums.ChatAction.TYPING)
    await asyncio.sleep(5)
    await client_obj.send_message(message_obj.chat.id, text)
    print(f"Ответили пользователю..")

@Client.on_message(filters.text)
async def text_handler(client, message):
    print(f"Пользователь отправил текст: {message.text}")
    await message_handler(client, message, "text")

@Client.on_message(filters.sticker)
async def sticker_handler(client, message):
    print(f"Пользователь отправил стикер: {message.text}")
    await message_handler(client, message, 'sticker')
