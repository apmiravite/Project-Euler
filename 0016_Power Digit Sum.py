# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(0,t):
    n=int(input())
    power=str(int(2**n))
    power_sum=0
    for j in range(0,len(power)):
        power_sum=power_sum+int(power[j])
    print(power_sum)
