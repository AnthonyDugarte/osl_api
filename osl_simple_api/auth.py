import hmac
import json
import hashlib
import base64

from osl_simple_api.helpers import remove_leading_slash


def rest_sign_token(data: dict, path: str, secret: str) -> bytes:
    hmac_obj = hmac.new(
        secret,
        (remove_leading_slash(path) + chr(0) + json.dumps(data)).encode('utf-8'),
        hashlib.sha512,
    )
    hmac_sign = base64.b64encode(hmac_obj.digest())

    return hmac_sign


def authorized_headers(key: str, data: dict, path: str, secret: str) -> str:
    hmac_sign = rest_sign_token(data=data, path=path, secret=secret)

    header = {
        'User-Agent': 'OSL API client',
        'Rest-Key': key,
        'Rest-Sign': hmac_sign,
    }

    return header
