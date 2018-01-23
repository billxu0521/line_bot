from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('ZRuOCy6WsqjtJy4kUQm9y1QSirLBqrCjLaI+Z5h6TyFjGwidjDSIROJjAxkybljCLgXE/0Ko5sO4+I8gByC+7yN3UMdBP46GsWIIyU8OzXQE/C6sBLSVCSYpS7UIGjkytL0WI4OT1p9Gqh+p3g+XAgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('019e45d02f962ae5c062880580cb9ff5')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    message = message + "幹你ㄇQ龍"
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
