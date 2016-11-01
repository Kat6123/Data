#!/usr/bin/python3

from re import compile
from input import ONE
from input import START
from request import request

BPS = "http://www.bps-sberbank.by/43257f17004e948d/dm_rates?open"


class DailyData():
    _pattern = {'buy': [], 'sale': []}

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)


def start_check(start, period):
    params = {'date': start.strftime(START)}
    r = request(BPS, params)
    if (parse(r.text) is None):
        print('Not found. Try another start date:')
        return False
    else:
        return True


def parse(html):
    au = compile(r'ЗОЛОТО')
    cost = compile(r'\d+?[,\. ]\d+')

    temp = au.search(html)
    if not(temp is None):
        data_list = cost.findall(html, au.search(html, temp.end()).end())
        return data_list
    else:
        return


def get_data(start, period):
    res = []
    temp = start
    for i in range(period):
        params = {'date': temp.strftime(START)}
        r = request(BPS, params)
        res.append(DailyData(parse(r.text)))
        temp += ONE
    return res
