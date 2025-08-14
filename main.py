from pyrogram import Client, filters

# अपने Telegram API क्रेडेंशियल्स
api_id = 27068302
api_hash = "5c844f554e418fe5cddb0867e0f9704a"

# यहां अपना असली string session डालो (Pyrogram string session tool से generate करो)
string_session = "Yaha_apna_STRING_SESSION_paste_karo"

# Client initialization — अब session_name= नहीं, सीधा string_session डालो
app = Client(string_session, api_id=api_id, api_hash=api_hash)

# एक साधारण इको हैंडलर
@app.on_message(filters.text)
def echo(client, message):
    message.reply_text("Hello! Bot is running successfully.")

# बॉट स्टार्ट करना
app.run()

