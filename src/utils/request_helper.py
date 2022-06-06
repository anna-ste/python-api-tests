import base64
import hashlib
import hmac
import urllib

import requests


def kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def kraken_post_request(base_url, uri_path, data, api_key, api_secret):
    headers = {'API-Key': api_key, 'API-Sign': kraken_signature(uri_path, data, api_secret)}

    # get_kraken_signature() as defined in the 'Authentication' section
    req = requests.post((base_url + uri_path), headers=headers, data=data)
    return req
