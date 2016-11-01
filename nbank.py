#!/usr/bin/python3

from input import ONE
from input import START
from request import request
from request import NBError

RUB = "http://www.nbrb.by/API/ExRates/Rates/298"
USD = "http://www.nbrb.by/API/ExRates/Rates/145"
FIELD = "Cur_OfficialRate"


class DailyData():
    def __init__(self, usd, rub):
        self.usd = usd
        self.rub = rub

    def __str__(self):
        return("USD: %f     RUB: %f" % (self.usd, self.rub))


def start_check(start, period):
    params = {'onDate': start.strftime(START)}
    try:
        request(USD, params)
        request(RUB, params)
    except NBError as e:
        print(e.message)
        return False


def get(resp):
    return resp.json().get(FIELD)


def get_data(start, period):
    res = []
    temp = start
    for i in range(period):
        params = {'onDate': temp.strftime(START)}
        res.append(DailyData(
            get(request(USD, params)),
            get(request(RUB, params))))
        temp += ONE
    return res
