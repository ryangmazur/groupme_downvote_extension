import os
import requests
import json
from typing import List
import time
from flask import Flask, request

class Bot():
    # Creates a GroupMe Bot to send message
    def __init__(self, bot_id: str):
        self.bot_id = bot_id

    def __repr__(self) -> str:
        return f"Bot {self.bot_id}"

    def send_message(self, text: str, attachments: List[str] = []) -> requests.Response:
        if DEBUG:
            print(f"send_message(): Attempting to send message: {text}")

        template = {
            "bot_id": self.bot_id,
            "text": text,
            "attachments": attachments
        }

        headers = {'content-type': 'application/json'}

        r = requests.post(POST_TO,
                        data = json.dumps(template), headers = headers)
        if r.status_code != 202:
            print(f"ERROR: message POST failed with code {r.status_code}")

        if DEBUG:
            print("send_message(): Successfully sent message")

        return r

# def parse():
#     print("In parse")

# # i think this will eventually need to take in an HTTP request and parse it to determine the function
# def main():
#     bot_id: str = os.environ["BOT_ID"]
#     test: str = os.environ["TEST"]
#     PORT: int = int(os.environ.get("PORT", 5000))
#     HOST: str = ''
#     bot: Bot = Bot(bot_id)

#     # if test:
#     #     # do stuff here if we want to test
#     #     print("test")
#     #     bot.send_message("Test Message")

#     # eventually need logic to determine what this should do

#     num: int = 1
#     while True:
#         bot.send_message(f"Test Message: {num}")
#         num += 1
#         time.sleep(30.0)


# if __name__ == "__main__":
#     main()


app = Flask(__name__)

DEBUG: str = (True if os.environ['BOT_DEBUG'] == 'True' else False)

BOT_ID: str = os.environ["BOT_ID"]
POST_TO: str = 'https://api.groupme.com/v3/bots/post'
bot: Bot = Bot(BOT_ID)

if DEBUG:
    print("Initialized all config values")


@app.route('/', methods=['POST'])
def webhook():
    if DEBUG:
        print("webhook(): Received post message")

    data = request.get_json()

    # test message
    msg: str = f"You said: {data['msg']}"
    bot.send_message(msg)