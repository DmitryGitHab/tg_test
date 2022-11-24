import time
from pyrogram import Client

"""
1. Создать множество каналов
2. добавить аватарки
3. Создать инвайт линк
"""

app = Client("account")

for _ in range(3):
    with app:
        chat = app.create_channel(f"channel{int(time.time())}", "Channel Description")

        with open('ava.png', 'rb') as file:
            app.set_chat_photo(chat_id=chat.id, photo=file)

        invite_link = app.get_chat(chat_id=chat.id)

    print(f"Канал создан, ссылка на канал: {invite_link.invite_link}")





