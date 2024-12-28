import time
from testing.data_store import append_price
import time
import requests
import urllib.parse
import hashlib
import hmac
import base64

import sys
import os
import strategies.live_momentum
from config import GlobalVars
import pandas as pd 

api_key = GlobalVars.api_key
api_secret = GlobalVars.api_secret
api_url = "https://api.kraken.com"

# signiature to send with request for verification
def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data["nonce"]) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def kraken_request(url_path, data, api_key, api_secret):
    headers = {"API-Key": api_key, "API-Sign": get_kraken_signature(url_path, data, api_secret)}
    resp = requests.post((api_url + url_path), headers=headers, data=data)
    return resp

# Get last trade closed price
def get_BTC_price_amount():
    resp = kraken_request("/0/public/Ticker?pair=BTCUSD", {"nonce": str(int(1000 * time.time()))} , api_key, api_secret)
    return (resp.json()["result"]["XXBTZUSD"]["c"][0])



def start_collecting_data():
    while True:
        time.sleep(120)
        price = float(get_BTC_price_amount())
        print (price)
        append_price(price)

        strategies.live_momentum.run_momentum_strategy()
        print(f"Collected new price: {price}")