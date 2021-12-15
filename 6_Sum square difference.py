#!/bin/python3

import sys

def square_of_sum(x):
    return (n*(n+1)*(1/2))**2

def sum_of_squares(x):
    return n*(n+1)*(2*n+1)*(1/6)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(int(square_of_sum(n))-int(sum_of_squares(n)))
