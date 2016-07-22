# coding=utf8

import time
import json
from attrdict import AttrDict

columns = 'abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ'

def test(loop_count):
    d1 = {a * 10: a * 20 for a in columns}
    d2 = {a * 10: a * 20 for a in columns}
    
    start = time.time()
    for _ in range(loop_count):
        a = d1['a' * 10]
        b = d1['b' * 10]
        c = d1['c' * 10]
        d = d1['d' * 10]
        d1['e' * 10] = d1['e' * 10][:-1] + '1'
        d1['f' * 10] = d1['f' * 10][:-1] + '1'
        d1['g' * 10] = d1['g' * 10][:-1] + '1'
        d1['h' * 10] = d1['h' * 10][:-1] + '1'
    end = time.time()
    print(d1)
    print(end - start, (end - start) / loop_count, start, end)

    ad = AttrDict(d2)
    start = time.time()
    for _ in range(loop_count):
        a = ad.aaaaaaaaaa
        b = ad.bbbbbbbbbb
        c = ad.cccccccccc
        d = ad.dddddddddd
        ad.eeeeeeeeee = ad.eeeeeeeeee[:-1] + '1'
        ad.ffffffffff = ad.ffffffffff[:-1] + '1'
        ad.gggggggggg = ad.gggggggggg[:-1] + '1'
        ad.hhhhhhhhhh = ad.hhhhhhhhhh[:-1] + '1'
    end = time.time()

    print(ad)
    print(d2)
    print(json.dumps(ad))
    print(end - start, (end - start) / loop_count, start, end)

if __name__ == '__main__':
    test(1000)
