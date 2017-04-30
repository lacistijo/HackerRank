#!/bin/python3

import sys


time = input().strip()

period = time[-2:]

if(period == "AM"):
    if(time[:2] == "12"):
        time_24 = "00:"+time[3:8]
    else:
        time_24 = time[0:8]
elif(period == "PM"):
    if(time[:2] == "12"):
        time_24 = time[0:8]
    else:
        time_24 = str(int(time[:2])+12)+time[2:8]
print(time_24)
    