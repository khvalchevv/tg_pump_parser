from pyrogram import Client, filters

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc"

TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 820

SOURCE_CHANNEL_USERNAME = "назва_каналу_з_пампами"  # без @

TOKENS = ["$pepe", "$wif", "$soon", "$dog", "$degen"]

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_USERNAME))
def forward_pumps(client, message):
    text = message.text.lower() if message.text else ""
    if any(token.lower() in text for token in TOKENS):
        client.send_message(
            chat_id=TARGET_CHAT_ID,
            message_thread_id=TARGET_THREAD_ID,
            text=f"🚀 New Pump Alert:\n\n{message.text}"
        )
        print(f"Forwarded: {message.text}")

app.run()
