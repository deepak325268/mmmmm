from pyrogram import Client, filters

api_id = 27068302
api_hash = "5c844f554e418fe5cddb0867e0f9704a"
string_session = "BQGdB44ACu-GxHjdwMsoKuLnlGP6Niaj7fHwYDntoIz_buOWU8cH-lVwm6WXbao1Qg2w9pAYKFDyltPruJea8x9JI4N2qYN2NPJvnh535DtGcnyjNnwHb9qO7IzsEjxO7Z_k70Y867OpU04axBza3U-EG4k3m4AlsvfNZTpPun8-uvzHLucqReusxa13nRVh4x2kAZREQluBFfv2RKHxXFEpZvAHLMT4n4PtZws7Muwvn3Uif0Io6bnt4jtlG1Yj-YZb-9ZbwfL6IUconWesxeaWdtXELNLINTMl9rDcMkyxXaupBq6-53zYD7-2HpcIftVYJhv9GuI7xdGRZCurLU2j6MEYTgAAAAGvulyOAA"

app = Client(
    name=":memory:",
    api_id=api_id,
    api_hash=api_hash,
    session_string=string_session
)

@app.on_message(filters.text)
def echo(client, message):
    message.reply_text("✅ Bot is running successfully!")

app.run()
