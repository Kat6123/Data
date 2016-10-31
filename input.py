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
            if not(today_check(date)):
                print("Today only %s!" % TODAY.strftime(START))
                continue
            break
        except ValueError:
            print("{YYYY}.{MM}.{DD}")
    return date


def period_input(start):
    print("Period:")
    while True:
        period = input()
        try:
            period = int(period)
            if (period >= MAX_PER):
                print("Too long!")
                continue
            finish = start+timedelta(days=period)
            if not(today_check(finish)):
                print("Finish %s is out of range!" % finish.strftime(START))
                continue
            break
        except ValueError:
            print("Only numbers!")
    return period


period_input(start_input())
