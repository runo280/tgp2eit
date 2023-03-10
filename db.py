# -*- coding: utf-8 -*-
import pymongo

from env import *

db_url = 'mongodb+srv://{user}:{pwd}@{murl}/?retryWrites=true&w=majority'
db_name = 'tg'
db_proxies = 'proxy'
db_date = 'data'
db_url = db_url.format(user=db_user, pwd=db_pass, murl=db_domain)
client = pymongo.MongoClient(db_url)
database = client[db_name]
proxies = database[db_proxies]


def update_session(_id, base):
    set_published_query = {'$set': {'session': base}}
    database[db_date].update_one({'_id': _id}, set_published_query)


def get_session():
    return database[db_date].find_one()


def add_to_db(proxy_list):
    for p in proxy_list:
        query = {'url': p.url}
        if proxies.count_documents(query) == 0:
            x = proxies.insert_one(p.get_dic())
            print(x.inserted_id)


def get_publish_queue():
    return proxies.find({"is_pub": False}).sort('_id', 1)


def set_published(tid):
    set_published_query = {'$set': {'is_pub': True}}
    proxies.update_one({'_id': tid}, set_published_query)
