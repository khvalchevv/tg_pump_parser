from pyrogram import Client, filters
import re

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc"

TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745

SOURCE_CHANNELS = ["dt_5p",]

FAVORITE_TOKENS = ["DBR", "ELDE", "GEAR", "TIBBIR", "WHITE"]

TOKEN_PATTERN = re.compile(r"\$([A-Z0-9]{2,10})\b")

ALL_SEEN_TOKENS = set()

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNELS))
def forward_pumps(client, message):
    text = message.text or ""
    tokens_in_message = set(match.group(1) for match in TOKEN_PATTERN.finditer(text.upper()))

    forwarded = False

    for token in tokens_in_message:
        if token in FAVORITE_TOKENS:
        
            client.send_message(
                chat_id=TARGET_CHAT_ID,
                message_thread_id=TARGET_THREAD_ID,
                text=f"🚀 FAVORITE TOKEN:\n\n${token}\n\n{text}"
            )
            print(f"Forwarded FAVORITE token: {token}")
            forwarded = True

        elif token not in ALL_SEEN_TOKENS:
            client.send_message(
                chat_id=TARGET_CHAT_ID,
                message_thread_id=TARGET_THREAD_ID,
                text=f"🎯 NEW TOKEN:\n\n${token}\n\n{text}"
            )
            print(f"Forwarded NEW token: {token}")
            ALL_SEEN_TOKENS.add(token)
            forwarded = True

    if not forwarded:
        print("No new or favorite token found in this message.")

app.run()
