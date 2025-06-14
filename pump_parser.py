from pyrogram import Client, filters
import asyncio

# --- Telegram API Keys ---
api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7775639673:AAEErQBi0PWD25B7SxM1xKu3kV2MR37DEeo"

# --- Target chat/thread and source channel ---
TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745
SOURCE_CHANNEL_USERNAME = "dt_5p"

# --- Whitelisted tokens ---
TOKENS = ["$dbr", "$elde", "$gear", "$tibbir", "$white", "$shm"]
seen_tokens = set(token.lower() for token in TOKENS)

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_USERNAME))
def handle_message(client, message):
    if not message.text:
        return

    text = message.text
    lower_text = text.lower()
    forwarded = False

    for token in TOKENS:
        if token.lower() in lower_text:
            client.copy_message(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=message.chat.id,
                message_id=message.id,
                message_thread_id=TARGET_THREAD_ID
            )
            print(f"✅ Forwarded (whitelisted): {text}")
            forwarded = True
            break

    # --- Detect and forward new token ---
    if not forwarded:
        words = text.split()
        new_tokens = [w for w in words if w.startswith("$") and w.lower() not in seen_tokens]
        if new_tokens:
            token = new_tokens[0]
            seen_tokens.add(token.lower())
            client.copy_message(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=message.chat.id,
                message_id=message.id,
                message_thread_id=TARGET_THREAD_ID
            )
            print(f"🆕 New token detected and forwarded: {token}")

# --- Optional: check access to the channel ---
async def check_access():
    try:
        chat = await app.get_chat(SOURCE_CHANNEL_USERNAME)
        print(f"💡 Доступ є! Канал: {chat.title} (ID: {chat.id})")
    except Exception as e:
        print(f"🔴 Помилка доступу: {e}. Бота треба додати в канал!")

app.run(check_access())
