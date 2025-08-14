from pyrogram import Client, filters

# आपके Telegram API डिटेल्स
api_id = 27068302
api_hash = "5c844f554e418fe5cddb0867e0f9704a"

# आपका String Session (पूरे का पूरा, एक लाइन में)
string_session = "BQGdB44AI9Cw7t-6Gozm_k6ryOjogaCzxAjc_nKh7r0etXc7Z2NUDsA8FOprqIrHEIlu6x3-gQChEr4-0DtDO6Y_q8fyk3eOu2t9z-k1Ko8weVfI6li4HiNlKtsWDsuXsBRMpoCSdGSDjEAwRsJWyBLAiV6KdymMl7IaYF9tk--A0NN05XupAwCPwfk73HMcadNjTkYaqGS8QANVARuO89YfCT78G2K_mqVmdRNs2cB2FZaoecR5RZtJhAgjaN5h7D_hRsck_q4dlXjshAS8Cj6PRzRVgSnv60IH-glPeF7w59QYPi6E8lLb3p_TRBYhMvLUHoCcqQt9LlknD4GQId_w_GqWgAAAAHzwlCPAQ"

# Pyrogram Client init (session_string के साथ)
app = Client(
    name=":memory:",  # Memory session ताकि कोई .session फाइल न बने
    api_id=api_id,
    api_hash=api_hash,
    session_string=string_session
)

# एक simple हैंडलर - चेक करने के लिए
@app.on_message(filters.text)
def echo(client, message):
    message.reply_text("✅ Bot is running successfully!")

# Bot शुरू करो
app.run()
