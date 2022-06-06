import time

import requests

from src.utils import helpers
from src.utils.settings_parser import settings


class ApiClient(object):

    def __init__(self, session=None):
        self.base_url = settings.base_url
        self.session = session or requests.Session()

    def get_server_time(self):
        return self.session.get(self.base_url + '/0/public/Time')

    def get_trading_pair(self, pair):
        return self.session.get(self.base_url + f'/0/public/AssetPairs?pair={pair}')


class SecureApiClient(ApiClient):

    def __init__(self, session=None):
        super().__init__(session)
        self.api_key = settings.api_key
        self.api_secret = settings.api_secret
        self.otp = settings.otp
        self.session = session or requests.Session()

    def retrieve_open_orders(self):
        uri_path = '/0/private/OpenOrders'
        data = {
            "nonce": str(int(1000 * time.time())),
            "otp": self.otp,
            "trades": True
        }
        headers = {'API-Key': self.api_key,
                   'API-Sign': helpers.kraken_signature(uri_path, data, self.api_secret)}

        # get_kraken_signature() as defined in the 'Authentication' section
        req = requests.post((self.base_url + uri_path), headers=headers, data=data)
        return req
