#!/usr/bin/python3

import input
import bps
import nbank

if __name__ == '__main__':
    start = input.start_input()
    period = input.period_input(start)
    try:
        bps.start_check(start, period)
        nbank.start_check(start, period)

        data = nbank.get_data(start, period)
        for i in data:
            print(i)
        data = bps.get_data(start, period)
        for i in data:
            print(i)
    except Exception:
        print("Error exit")
