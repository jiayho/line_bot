from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


#權杖
line_bot_api = LineBotApi('gXZ4aU3ROFYxbFWRd1BiI/4vo3E4693xQWksff3HwDKTt+u2Fx7sGOQrw5hDJfDdKTgWDh0mxqv+byr5ikoXThQkOuaauOkvm1ISRtXc0ZOijmgJ22hdl+7VOVQSpPDpd3IDOmdDauzDFXyslKorMgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5a497980dd507977111a0826abf36c78')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mag = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="你吃飯了嗎"))


if __name__ == "__main__":
    app.run()