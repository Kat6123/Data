#!/usr/bin/python3

from datetime import timedelta
from datetime import datetime

ONE = timedelta(days=1)
START = "%Y.%m.%d"
TODAY = datetime.today()
MAX_PER = 365


def today_check(date):
    if (TODAY - date).days < 0:
        return False
    return True


def start_input():
    print("Start:")
    while True:
        date = input()
        try:
            date = datetime.strptime(date, START)
        except ValueError:
            print("{YYYY}.{MM}.{DD}")
            continue
        if not(today_check(date)):
            print("Today only %s!" % TODAY.strftime(START))
            continue
        break
    return date


def period_input(start):
    print("Period:")
    while True:
        period = input()
        try:
            period = int(period)
        except ValueError:
            print("Only numbers!")
            continue
        if (period > MAX_PER or period <= 0):
            print("Range: 1..365!")
            continue
        finish = start+timedelta(days=period-1)
        if not(today_check(finish)):
            print("Finish %s is out of range!" % finish.strftime(START))
            continue
        break
    return period
