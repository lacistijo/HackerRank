# by Laszlo Tatai
# created on 2017.04.19
# Diagonal Difference

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

r=0
c=0
pdiag=0
sdiag=0

for row in a:
    for col in row:
        if(r == c):
            pdiag += a[r][c]
        if(c == (n-r-1)):
            sdiag += a[r][c]
        if(c == n-1):
            c = -1
        c+=1    
    r+=1    
res = abs(pdiag-sdiag)    
print(res)
    