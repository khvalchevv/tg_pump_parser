from pyrogram import Client, filters

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc"

TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745
SOURCE_CHANNEL_USERNAME = "dt_5p"  # без @

# Випиши свої токени (з $ або без — не важливо)
TOKENS = ["$dbr", "$elde", "$gear", "$tibbir", "$white", "$shm"]

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_USERNAME))
async def handler(client, message):
    text = message.text.lower() if message.text else ""
    if any(token.lower() in text for token in TOKENS):
        await client.forward_messages(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=SOURCE_CHANNEL_USERNAME,
            message_ids=message.message_id,
            message_thread_id=TARGET_THREAD_ID
        )
        print(f"✅ Forwarded: {message.text}")
    else:
        print(f"⏭ Skipped: {message.text}")

app.run()
