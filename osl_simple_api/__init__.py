import base64
import os
import requests

from osl_simple_api.auth import authorized_headers
from osl_simple_api.helpers import remove_leading_slash, gen_osl_tonce


class OslClient:
    def __init__(
        self,
        key: str = os.getenv('OSL_KEY'),
        secret: str = os.getenv('OSL_SECRET'),
        base_url: str = 'https://trade.osl.com/',
    ):
        self.key = key
        self.secret = base64.b64decode(secret)
        self.base_url = base_url

    def request(self, path: str, data: dict = {}, method="POST"):
        path = remove_leading_slash(path)

        data = data.copy()
        data.update({'tonce': gen_osl_tonce()})

        headers = authorized_headers(
            key=self.key,
            data=data,
            path=path,
            secret=self.secret
        )

        url = "%s%s" % (self.base_url, path)

        r = requests.request(
            method=method,
            url=url,
            json=data,
            headers=headers,
        )

        return r.json()
