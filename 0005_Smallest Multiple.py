#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lcm=1
    for factor in range(1,n+1):
        lcm=int((lcm*factor)/math.gcd(lcm, factor))
    print(lcm)
        
