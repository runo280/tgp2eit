import base64
from collections.abc import Iterable

from telethon.tl.types import MessageEntityTextUrl

import db
from Telegram import MyTelegram
from api import *
from env import *

if __name__ == "__main__":

    # get tg session
    squery = db.get_session()
    decoded_string = base64.b64decode(squery['session'])
    with open("seasion.session", "wb") as sfile:
        sfile.write(decoded_string)

    tg = MyTelegram('seasion.session', api_id, api_hash, phone_number, password)

    peers = target_peer.split('|')
    # print(peers)
    for peer_id in peers:
        name = tg.get_channel_name(int(peer_id)).username
        for p in tg.get_latest_posts(int(peer_id)):
            # print(p.message)
            # print(name)
            r = send_message(p.message + "\n\n#" + name)
            # print(r)

    with open("seasion.session", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        db.update_session(squery['_id'], b64_string)
