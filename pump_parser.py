import os
from pyrogram import Client

app = Client(
    "my_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

print("🟢 Бот стартував! Очікуємо повідомлень...")

@app.on_message(filters.chat("dt_5p"))
async def handler(client, message):
    print(f"📥 Отримано: {message.text}")
    await message.forward(-1002604238211)  # Ваш TARGET_CHAT_ID

app.run()
