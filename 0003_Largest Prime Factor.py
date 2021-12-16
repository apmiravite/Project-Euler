import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    largest_prime=1
    for i in range(1, math.floor(math.sqrt(n))+1):
        if n%i==0:
            f_1=i
            f_2=n/i
            factorcounter1=0
            factorcounter2=0
            for factor in range(1, math.floor(math.sqrt(f_1))+1):
                if f_1%factor==0:
                    factorcounter1=factorcounter1+1
            for factor in range(1, math.floor(math.sqrt(f_2))+1):
                if f_2%factor==0:
                    factorcounter2=factorcounter2+1
            if factorcounter1==1 and factorcounter2!=1:
                largestprime=f_1
            elif factorcounter1!=1 and factorcounter2==1:
                largestprime=f_2
            elif factorcounter1==1 and factorcounter2==1: 
                largestprime=f_2
    print(int(largestprime))
