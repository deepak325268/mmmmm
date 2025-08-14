from pyrogram import Client, filters

# अपने Telegram API क्रेडेंशियल्स
api_id = 27068302
api_hash = "5c844f554e418fe5cddb0867e0f9704a"

# यहां अपना असली string session डालो (Pyrogram string session tool से generate करो)
string_session = "BQGdB44AI9Cw7t-6Gozm_k6ryOjogaCzxAjc_nKh7r0etXc7Z2NUDsA8FOprqIrHEIlu6x3-gQChEr4-0DtDO6Y_q8fyk3eOu2t9z-k1Ko8weVfI6li4HiNlKtsWDsuXsBRMpoCSdGSDjEAwRsJWyBLAiV6KdymMl7IaYF9tk-_-A0NN05XupAwCPwfk73HMcadNjTkYaqGS8QANVARuO89YfCT78G2K_mqVmdRNs2cB2FZaoecR5RZtJhAgjaN5h7D_hRsck_q4dlXjshAS8Cj6PRzRVgSnv60IH-glPeF7w59QYPi6E8lLb3p_TRBYhMvLUHoCcqQt9LlknD4GQId_w_GqWgAAAAHzwlCPAQ"

# Client initialization — अब session_name= नहीं, सीधा string_session डालो
app = Client(string_session, api_id=api_id, api_hash=api_hash)

# एक साधारण इको हैंडलर
@app.on_message(filters.text)
def echo(client, message):
    message.reply_text("Hello! Bot is running successfully.")

# बॉट स्टार्ट करना
app.run()

