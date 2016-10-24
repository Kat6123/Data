#!/usr/bin/python3

import requests
import re

if __name__ == '__main__':
    start = input("Start:")
    col = int(input("How much:"))
    data = re.compile(r"\d+$", re.M)
    day = data.search(start).group(0)
    start = data.sub('', start)
    cost = re.compile(r'\d+?[,\. ]\d+')
    au = re.compile('ЗОЛОТО')
    for i in range(col):
        r = requests.get(
            'http://www.bps-sberbank.by/43257f17004e948d/dm_rates?open',
            params={'date': start+day})
        l = cost.findall(
            r.text,
            au.search(r.text, au.search(r.text).end()).end())
        print(l)
        day = str(int(day) + 1)
