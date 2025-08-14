from pyrogram import Client

api_id = 27068302
api_hash = "5c844f554e418fe5cddb0867e0f9704a"
string_session = "Yaha tumhara string session paste karo"

app = Client(session_name=string_session, api_id=api_id, api_hash=api_hash)

@app.on_message()
def echo(client, message):
    message.reply_text("Hello! Bot is running successfully.")

app.run()
