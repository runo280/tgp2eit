# -*- coding: utf-8 -*-
class Proxy:
    def __init__(self, url, is_published=False):
        self.url = url
        self.is_published = is_published

    def get_dic(self):
        return {'url': self.url, 'is_pub': self.is_published}
