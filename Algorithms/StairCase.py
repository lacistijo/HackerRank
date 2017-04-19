#!/bin/python3

import sys

n = int(input().strip())

def printstair(num, n):
    space = " "*(num-1)
    hasht = "#"*(n-(num-1))
    print(space+hasht)
    if(num > 1):
        printstair(num-1, n)

printstair(n, n) 