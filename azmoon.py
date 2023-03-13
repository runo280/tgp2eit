# -*- coding: utf-8 -*-
import base64

from telethon.tl.types import DocumentAttributeFilename, Message

import db
from Telegram import MyTelegram
from api import *
from mutil import *
import time

ch_id = -1001982256525

if __name__ == "__main__":
    # get tg session
    if not is_offline():
        session_query = db.get_session()
        decoded_string = base64.b64decode(session_query['session'])
        with open("seasion.session", "wb") as session_file:
            session_file.write(decoded_string)

    tg = MyTelegram('seasion.session', api_id,
                    api_hash, phone_number, password)

    for p in tg.get_latest_posts(ch_id, 100):
        if isinstance(p, Message):
            time.sleep(10)
            print(p.stringify())
            text = p.message
            filename_attr = next(filter(lambda x: isinstance(x, DocumentAttributeFilename),
                                        p.document.attributes), None)
            filename = filename_attr.file_name if filename_attr else 'Unknown'
            filename = filename.replace(" ", "_")
            print(filename)
            length = len(text)
            if p.file:
                print('has file')
                p.download_media(file=filename)
                if length < 1400:
                    r = send_file(text, filename)
                    print(r)
                    # delete_msg_file(filename)
                else:
                    r = send_file("", filename)
                    time.sleep(30)
                    print(r)
                    r2 = send_message(text)
                    # delete_msg_file(filename)

    # save tg session
    if not is_offline():
        with open("seasion.session", "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            db.update_session(session_query['_id'], b64_string)
