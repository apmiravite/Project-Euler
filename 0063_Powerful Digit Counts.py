import math

n=int(input())
counter=int(0)

for num in range(1, 10):
    if num**n >=10**(n-1) and num**n <10**n:
        print_me=num**n
        print(print_me)
