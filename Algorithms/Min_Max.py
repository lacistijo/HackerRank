#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

nums = [a,b,c,d,e]
work = [a,b,c,d,e]
size = len(nums)
mini = 0
maxi = 0

for i in range(size):
    nums[i] = 0
    add = 0
    for elem in nums:
        add += elem
    nums[i] = work[i]
    if(i == 0):
        mini = add
        maxi = add
    elif(add > maxi):
        maxi = add
    elif(add < mini):
        mini = add
print(str(mini)+" "+str(maxi))