#!/usr/bin/python3

import requests

TIMEOUT = 180
ERROR = 404


class RError(Exception):
    def __init__(self, message):
        self.message = message


def request(url, param):
    try:
        req = requests.get(url, params=param, timeout=TIMEOUT)
    except requests.ConnectionError:
        raise RError('Network problem')
    except requests.Timeout:
        raise RError('Request times out')
    if not(req.status_code == requests.codes.ok):
        if (req.status_code == ERROR):
            raise RError("Not found. Try another date:")
        raise RError('Response code: %d" % req.status_code')
    return req
