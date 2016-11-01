#!/usr/bin/python3

import requests

TIMEOUT = 180
ERROR = 404


class NBError(Exception):
    def __init__(self, message):
        self.message = message


def request(url, param):
    try:
        req = requests.get(url, params=param, timeout=TIMEOUT)
    except requests.ConnectionError:
        print('Network problem')
        raise
    except requests.Timeout:
        print('Request times out')
        raise
    if not(req.status_code == requests.codes.ok):
        print("Response code: %d" % req.status_code)
        if (req.status_code == ERROR):
            raise NBError("Not found. Try another date:")
        raise
    return req
