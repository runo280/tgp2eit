import os
#import configparser

#account_config = "config.conf"
#config = configparser.RawConfigParser(allow_no_value=False)
# config.read(account_config)


phone_number = os.environ['tgPhone']
password = os.environ['tgPass']

api_id = os.environ['apiId']
api_hash = os.environ['apiHash']

bot_token = os.environ['botToken']
channel_id = os.environ['peerId']
api_url = os.environ['apiUrl']

replace_str = os.environ['replaceStr'].split('^')

target_peer = os.environ['targetPeer']


db_user = os.environ['muser']
db_pass = os.environ['mpass']
db_domain = os.environ['murl']
