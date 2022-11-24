from env import *
from os.path import isfile
import requests
import json


def cleanCaption(caption):
    return caption.replace('tg://proxy', 'https://t.me/proxy')


def send_message(text, pin=False, view_to_delete=-1,
                 disable_notification=False, reply_to_message_id=None):
    http_proxy = "http://127.0.0.1:7890"
    https_proxy = "http://127.0.0.1:7890"

    proxies = {
        "http": http_proxy,
        "https": https_proxy
    }

    r = requests.post(
        f"https://{api_url}/api/{bot_token}/sendMessage",
        data={
            'chat_id': channel_id,
            'text': cleanCaption(text),
            'pin': int(pin),
            'viewCountForDelete': view_to_delete,
            'disable_notification': int(disable_notification),
            'reply_to_message_id': reply_to_message_id if reply_to_message_id != None else '',
        }
        , proxies=proxies
    )
    return json.loads(r.text)
