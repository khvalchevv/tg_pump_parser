from pyrogram import Client, filters
import re

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc"

TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745
SOURCE_CHANNEL_USERNAME = "dt_5p"

TOKENS = ["$dbr", "$elde", "$gear", "$tibbir", "$white", "shm", "anime"]

# Створюємо set для унікальних нових токенів:
seen_tokens = set()

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_USERNAME))
def forward_pumps(client, message):
    text = (message.text or message.caption or "").lower()

    # 1️⃣ Якщо whitelist токен
    if any(token.lower() in text for token in TOKENS):
        client.forward_messages(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=message.chat.id,
            message_ids=message.id,
            message_thread_id=TARGET_THREAD_ID
        )
        print(f"[WHITELIST] Forwarded message ID: {message.id}")

    # 2️⃣ Шукаємо нові токени $XXX
    matches = re.findall(r'\$[a-zA-Z0-9]+', text)

    for token in matches:
        token_lower = token.lower()
        if token_lower not in seen_tokens and token_lower not in [t.lower() for t in TOKENS]:
            seen_tokens.add(token_lower)

            client.forward_messages(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=message.chat.id,
                message_ids=message.id,
                message_thread_id=TARGET_THREAD_ID
            )
            print(f"[NEW TOKEN] {token} → Forwarded message ID: {message.id}")

app.run()
