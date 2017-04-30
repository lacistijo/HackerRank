#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

blow = 0
temp = 0

for hght in height:
    if(hght > temp):
        temp = hght
        blow = 1
    elif(hght == temp):
        blow += 1
print(blow)