import os
from pyrogram import Client, filters  # Додано імпорт filters!

app = Client(
    "my_bot",
    api_id=int(os.getenv("API_ID", 22929642)),  # Значення за замовчуванням
    api_hash=os.getenv("API_HASH", "9e1cb2954a8822c811fa4f0e78a9ffe4"),
    bot_token=os.getenv("BOT_TOKEN", "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc")
)

print("🟢 Бот стартував! Очікуємо повідомлень...")

@app.on_message(filters.chat("dt_5p"))  # Тепер filters визначено
async def handler(client, message):
    print(f"📥 Отримано: {message.text}")
    await message.forward(-1002604238211)  # Ваш TARGET_CHAT_ID

app.run()
