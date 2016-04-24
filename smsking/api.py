# coding: utf-8

import re

import requests

from .exceptions import SMSKingErrorResponse
from .exceptions import SMSKingErrorCodeResponse


KMSGID_RE = re.compile(r'kmsgid=(-?\d+)')


class SMSKingAPIClient(object):
    """
    簡訊王 簡訊 API
    http://www.kotsms.com.tw/index.php?selectpage=pagenews&kind=4&viewnum=238
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.base_url = 'https://api.kotsms.com.tw'
        self.send_sms_endpoint = '/kotsmsapi-1.php'
        self.send_mass_sms_endpoint = '/kotsmsapi-2.php'

    def make_request(self, endpoint, *args, **kwargs):
        r = requests.get(endpoint, *args, **kwargs)

        kmsgid_match = KMSGID_RE.search(r.text)
        if not kmsgid_match:
            raise SMSKingErrorResponse(r.url, r.status_code, r.content)

        kmsgid = int(kmsgid_match.group(1))

        if kmsgid < 0:
            raise SMSKingErrorCodeResponse(r.url, r.status_code, r.content, kmsgid)

        return kmsgid

    def convert_to_big5(self, text):
        try:
            big5_text = text.encode('big5')
        except UnicodeDecodeError:
            big5_text = text.decode('utf-8').encode('big5')

        return big5_text

    def send_sms(self, dstaddr, smbody, response=None):
        """
        即時 API
        """

        endpoint = '{0}{1}'.format(self.base_url, self.send_sms_endpoint)
        payload = {
            'username': self.username,
            'password': self.password,
            'dstaddr': dstaddr,
            'smbody': self.convert_to_big5(smbody),
        }

        if response:
            payload['response'] = response

        return self.make_request(endpoint, params=payload)

    # TODO
    def send_mass_sms(self):
        """
        大量 API
        """

        raise NotImplementedError()
