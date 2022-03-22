import os
import requests as req
import json
from typing import List

class Bot():
    # Creates a GroupMe Bot to send message
    def __init__(self, bot_id: str):
        self.bot_id = bot_id

    def __repr__(self) -> str:
        return f"Bot {self.bot_id}"

    def send_message(self, text: str, attachments: List[str] = []) -> req.Response:
        template = {
            "bot_id": self.bot_id,
            "text": text,
            "attachments": attachments
        }

        headers = {'content-type': 'application/json'}

        r = req.post("https://api.groupme.com/v3/bots/post",
                        data = json.dumps(template), headers = headers)
        if r.status_code != 202:
            print(f"ERROR: message POST failed with code {r.status_code}")

        return r

# i think this will eventually need to take in an HTTP request and parse it to determine the function
def bot_main(function):
    bot_id: str = os.environ["BOT_ID"]
    test: str = os.environ["TEST"]

    bot: Bot = Bot(bot_id)

    if test:
        # do stuff here if we want to test
        bot.send_message("Test Message")

    # eventually need logic to determine what this should do

