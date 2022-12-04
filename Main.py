import base64
from collections.abc import Iterable

from telethon.tl.types import MessageEntityTextUrl

import db
from Telegram import MyTelegram
from api import *
from env import *
from post import Proxy


def add2list(mlist, item):
    if 'https://t.me/proxy?server' in item or 'tg://proxy?server' in item:
        mlist.append(item)


if __name__ == "__main__":

    # get tg session
    squery = db.get_session()
    decoded_string = base64.b64decode(squery['session'])
    with open("seasion.session", "wb") as sfile:
        sfile.write(decoded_string)

    tg = MyTelegram('seasion.session', api_id,
                    api_hash, phone_number, password)

    unique_list = []
    peers = target_peer.split('|')
    print(peers)
    for peer_id in peers:
        for p in tg.get_latest_posts(int(peer_id)):
            if hasattr(p, 'reply_markup'):
                if hasattr(p.reply_markup, 'rows'):
                    for r in p.reply_markup.rows:
                        for kr in r.buttons:
                            add2list(unique_list, kr.url)
            if hasattr(p, 'entities'):
                if isinstance(p.entities, Iterable):
                    for e in p.entities:
                        if isinstance(e, MessageEntityTextUrl):
                            add2list(unique_list, e.url)

    unique_list = list(set(unique_list))

    list_to_db = []
    for url in unique_list:
        proxy = Proxy(url)
        list_to_db.append(proxy)
    db.add_to_db(list_to_db)

    for p in db.get_publish_queue():
        r = send_message(p['url'])
        if r['ok']:
            db.set_published(p['_id'])

    # save tg session
    with open("seasion.session", "rb") as img_file:
        b64_string = base64.b64encode(img_file.read())
        db.update_session(squery['_id'], b64_string)
