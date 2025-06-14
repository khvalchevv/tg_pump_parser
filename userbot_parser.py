from telethon import TelegramClient, events
import asyncio
import os

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"

session_name = "user_session"  # ім'я сесії .session-файлу

# Цільові параметри
SOURCE_CHANNEL = "dt_5p"  # Канал з якого парсиш
TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745
TOKENS = ["$dbr", "$elde", "$gear", "$tibbir", "$white", "$shm"]

# Ініціалізація клієнта
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    text = event.raw_text.lower()
    if any(token.lower() in text for token in TOKENS):
        await client.forward_messages(
            entity=TARGET_CHAT_ID,
            messages=event.message,
            thread_id=TARGET_THREAD_ID
        )
        print(f"✅ Forwarded: {event.raw_text}")
    else:
        print(f"⛔ Skipped: {event.raw_text}")

async def main():
    me = await client.get_me()
    print(f"🤖 Logged in as: {me.username}")

client.start()
client.loop.run_until_complete(main())
client.run_until_disconnected()
