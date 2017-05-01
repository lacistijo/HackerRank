#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    summ = 0
    for val in range(n):
        if((val % 5 == 0) or (val % 3 == 0)):
            summ += val
    print(summ)