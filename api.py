import json
from os.path import isfile

import requests

from env import *


def clean_caption(caption):
    return caption.replace('tg://proxy', 'https://t.me/proxy')


def send_message(text, pin=False, view_to_delete=-1,
                 disable_notification=False, reply_to_message_id=None):
    r = requests.post(
        f"https://{api_url}/api/{bot_token}/sendMessage",
        data={
            'chat_id': channel_id,
            'text': clean_caption(text),
            'pin': int(pin),
            'viewCountForDelete': view_to_delete,
            'disable_notification': int(disable_notification),
            'reply_to_message_id': reply_to_message_id if reply_to_message_id is not None else '',
        }
    )
    return json.loads(r.text)


def send_file(text, file, pin=False, view_to_delete=-1,
              disable_notification=False, reply_to_message_id=None):
    if not isfile(file):
        raise Exception(f"File `{file}` not found")

    r = requests.post(
        f"https://{api_url}/api/{bot_token}/sendFile",
        data={
            'chat_id': 8552039,
            'caption': clean_caption(text),
            'pin': int(pin),
            'viewCountForDelete': view_to_delete,
            'disable_notification': int(disable_notification),
            'reply_to_message_id': reply_to_message_id if reply_to_message_id is not None else '',
        },
        files={
            'file': open(file, 'rb'),
        }
    )
    return json.loads(r.text)
