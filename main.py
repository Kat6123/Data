#!/usr/bin/python3

import input
import bps
import nbank
from request import RError

if __name__ == '__main__':
    start = input.start_input()
    period = input.period_input(start)
    try:
        bps.start_check(start, period)

        data = bps.get_data(start, period)
        for i in data:
            print(i)
        data = nbank.get_data(start, period)
        for i in data:
            print(i)
    except RError as e:
        print(e.message)
