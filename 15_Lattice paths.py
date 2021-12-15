# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

t=int(input())
for i in range(0,t):
    n, m = map(int, input().split())
    print(int((factorial(n+m)//factorial(n)//factorial(m))%(10**9+7)))
