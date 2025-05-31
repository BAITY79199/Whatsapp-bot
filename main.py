from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg:
        response_text = f"Hujambo! Umetuma: {incoming_msg}"
    else:
        response_text = "Habari! Karibu kwenye WhatsApp bot."

    msg.body(response_text)
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
