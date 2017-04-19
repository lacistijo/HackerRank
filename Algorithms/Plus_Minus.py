#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

plus=0
minus=0
zero=0

for val in arr:
    if(val > 0):
        plus += 1
    elif(val < 0):
        minus += 1
    else:
        zero += 1
        
print("{:.6f}".format(plus/n))
print("{:.6f}".format(minus/n))
print("{:.6f}".format(zero/n))