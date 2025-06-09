import os
from pyrogram import Client, filters

# Налаштування (значення за замовчуванням для локального тесту)
api_id = int(os.getenv("API_ID", 22929642))
api_hash = os.getenv("API_HASH", "9e1cb2954a8822c811fa4f0e78a9ffe4")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc")

# ID чату для пересилання (з мінусом для груп)
TARGET_CHAT_ID = -1002604238211
# ID гілки (якщо потрібно)
TARGET_THREAD_ID = 1745
# Канал для моніторингу (без @)
SOURCE_CHANNEL = "dt_5p"

# Список токенів для відстеження (без $)
TOKENS = ["DBR", "ELDE", "GEAR", "TIBBIR", "WHITE", "SHM", "KBBB", "EGL1"]
# Множина відомих токенів
SEEN_TOKENS = set(TOKENS)
# Лічильник нових токенів
NEW_TOKEN_COUNTER = {}
# Максимальна кількість пересилань для нового токену
MAX_NEW_TOKEN_FORWARDS = 5

# Ініціалізація клієнта
app = Client(
    "pump_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=BOT_TOKEN
)

print("🟢 Бот ініціалізовано! Очікуємо повідомлень...")

def extract_token(text):
    """Витягує токен з повідомлення (формат '$TAG')"""
    lines = text.split('\n')
    if not lines:
        return None
    
    first_line = lines[0].strip()
    if first_line.startswith('🟢 $'):
        return first_line.split('$')[1].split()[0].upper()
    return None

@app.on_message(filters.chat(SOURCE_CHANNEL))
async def handle_message(client, message):
    try:
        text = message.text or message.caption or ""
        print(f"\n📥 Нове повідомлення з каналу:\n{text[:200]}...")

        # Перевірка на зелений кружець
        if not text.startswith('🟢'):
            print("🔴 Ігноруємо: немає зеленого кружечка")
            return

        # Витягуємо токен
        token = extract_token(text)
        if not token:
            print("❌ Не знайдено токену у повідомленні")
            return

        print(f"🔍 Токен: {token}")

        # Пересилання повідомлення
        await client.forward_messages(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=message.chat.id,
            message_ids=message.id,
            message_thread_id=TARGET_THREAD_ID
        )
        print(f"✅ Успішно переслано токен {token}!")

    except Exception as e:
        print(f"‼️ Критична помилка: {str(e)}")

# Запуск бота
app.run()
