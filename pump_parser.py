from pyrogram import Client, filters

api_id = 22929642
api_hash = "9e1cb2954a8822c811fa4f0e78a9ffe4"
BOT_TOKEN = "7598909276:AAHJ15EyR2390Ke7hVQ4hq94yTiajX3tDGc"

TARGET_CHAT_ID = -1002604238211
TARGET_THREAD_ID = 1745
SOURCE_CHANNEL_USERNAME = "dt_5p"

# Initial whitelist
TOKENS = ["$DBR", "$ELDE", "$GEAR", "$TIBBIR", "$WHITE", "$SHM", "kbbb"]

SEEN_TOKENS = set(token.upper() for token in TOKENS)
NEW_TOKEN_COUNTER = {}  # нові токени → рахунок форвардів

MAX_NEW_TOKEN_FORWARDS = 5  # після 5 сповіщень токен вважається "запам’ятаним"

app = Client("pump_parser", api_id=api_id, api_hash=api_hash, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(SOURCE_CHANNEL_USERNAME))
def forward_pumps(client, message):
    text = (message.text or message.caption or "")

    tokens_in_msg = [word for word in text.split() if word.startswith("$")]

    for token in tokens_in_msg:
        token_upper = token.upper()

        if token_upper in SEEN_TOKENS:
            # Токен вже в whitelist → форвардимо
            client.forward_messages(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=message.chat.id,
                message_ids=message.id,
                message_thread_id=TARGET_THREAD_ID
            )
            print(f"✅ Forwarded WHITELIST token: {token_upper}")
            return

        # Новий токен → лічимо скільки разів вже форвардили
        count = NEW_TOKEN_COUNTER.get(token_upper, 0)

        if count < MAX_NEW_TOKEN_FORWARDS:
            client.forward_messages(
                chat_id=TARGET_CHAT_ID,
                from_chat_id=message.chat.id,
                message_ids=message.id,
                message_thread_id=TARGET_THREAD_ID
            )
            NEW_TOKEN_COUNTER[token_upper] = count + 1
            print(f"🚀 Forwarded NEW token: {token_upper} ({NEW_TOKEN_COUNTER[token_upper]}/{MAX_NEW_TOKEN_FORWARDS})")

            if NEW_TOKEN_COUNTER[token_upper] == MAX_NEW_TOKEN_FORWARDS:
                SEEN_TOKENS.add(token_upper)
                print(f"🎉 Token {token_upper} added to memory after {MAX_NEW_TOKEN_FORWARDS} forwards.")
            return  # після першого знайденого токену досить форвардити це повідомлення

app.run()
