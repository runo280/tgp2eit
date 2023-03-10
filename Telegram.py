from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, PeerChannel
import utils


class MyTelegram:
    _name = ''
    _api_id = 0
    _api_hash = ''
    _phone_number = ''
    _password = ''
    _client = None
    _dialogs = None

    def __init__(self, name, api_id, api_hash, phone, password):
        self._name = name
        self._api_id = api_id
        self._api_hash = api_hash
        self._phone_number = phone
        self._password = password

        self._client = TelegramClient(self._name, self._api_id, self._api_hash, proxy=(
            "socks5", '127.0.0.1', 2080)) if (utils.is_offline()) else TelegramClient(self._name, self._api_id,
                                                                                      self._api_hash)

        self._client.connect()

        if not self._client.is_user_authorized():
            print('Not authorized')
            self._client.send_code_request(self._phone_number)
            try:
                self._client.sign_in(self._phone_number,
                                     input('Enter code:\n'))
            except SessionPasswordNeededError:
                self._client.sign_in(password=self._password)

        if self._client.is_user_authorized():
            print('Authorized')

        self._dialogs = self._client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=500,
            hash=1
        ))

    def get_latest_posts(self, peer_id):
        return self._client.get_messages(peer_id, limit=20)

    def get_message_by_id(self, peer_id, post_id):
        return self._client.get_messages(peer_id, ids=post_id)

    def get_latest_post_id(self, peer_id):
        return self._client.get_messages(peer_id)[0].id

    def get_channel_name(self, peer_id):
        return self._client.get_entity(PeerChannel(peer_id))
