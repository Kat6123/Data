#!/usr/bin/python3

from re import compile
from input import ONE
from input import START
from request import request
from request import RError

BPS = "http://www.bps-sberbank.by/43257f17004e948d/dm_rates?open"


class DailyData():
    def __init__(self, list):
        self.au = dict(buy=list[0:2], sale=list[2:4])
        self.ag = dict(buy=list[4:6], sale=list[6:8])
        self.pt = dict(buy=list[8:10], sale=list[10:12])
        self.pd = dict(buy=list[12:14], sale=list[14:16])

    def __newstr(self, arg):
        return(''.join([
            "{0}     {1}".format(*arg['buy']),
            "        ",
            "{0}     {1}".format(*arg['sale'])]))

    def __str__(self):
        return (''.join([
            "               Buy:                    Sale:"
            "\nGold           ", self.__newstr(self.au),
            "\nSilver         ", self.__newstr(self.ag),
            "\nPlatinum       ", self.__newstr(self.pt),
            "\nPalladium      ", self.__newstr(self.pd)]))


def start_check(start, period):
    params = {'date': start.strftime(START)}
    r = request(BPS, params)
    if (parse(r.text) is None):
        raise RError('Not found. Try another start date:')


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
