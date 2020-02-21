#PYTHON 3.4
import requests
import json
import base64
import hashlib
import time
import hmac

bitfinexURL = 'https://api.bitfinex.com/v1/balances'
bitfinexKey = 'NWioXIhZZhCTOcxP5k6CQeeTTWXX4URvcgvB1SjwTIB'
bitfinexSecret = b'4k5MAi2yPTu6dh74PWYcu1sHiTyakrxa5C4Ti5ocH2e' #the b is deliberate, encodes to bytes

def start():
    print("BitFinex")
    payloadObject = {
            'request':'/v1/balances',
            'nonce':str(time.time() * 100000), #convert to string
            'options':{}
    }

    payload_json = json.dumps(payloadObject)
    print("payload_json: ", payload_json)

    payload = base64.b64encode(bytes(payload_json, "utf-8"))
    print("payload: ", payload)

    m = hmac.new(bitfinexSecret, payload, hashlib.sha384)
    m = m.hexdigest()

    #headers
    headers = {
          'X-BFX-APIKEY' : bitfinexKey,
          'X-BFX-PAYLOAD' : base64.b64encode(bytes(payload_json, "utf-8")),
          'X-BFX-SIGNATURE' : m
    }

    r = requests.get(bitfinexURL, data={}, headers=headers)
    print('Response Code: ' + str(r.status_code))
    print('Response Header: ' + str(r.headers))
    print('Response Content: '+ str(r.content))