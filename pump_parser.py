from pyrogram import Client, filters

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc"

TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745
SOURCE_CHANNEL_USERNAME = "dt_5p"

# Вписуй сюди свої токени (з $ або без, всі будуть приведені до нижнього регістру)
TOKENS = ["$dbr", "$elde", "$gear", "$tibbir", "$white", "$shm"]

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_USERNAME))
def handler(client, message):
    if not message.text:
        return
    text = message.text.lower()
    if any(token.lower() in text for token in TOKENS):
        client.send_message(
            chat_id=TARGET_CHAT_ID,
            message_thread_id=TARGET_THREAD_ID,
            text=message.text
        )
        print(f"✅ Forwarded: {message.text}")
    else:
        print(f"❌ Skipped: {message.text}")

app.run()
