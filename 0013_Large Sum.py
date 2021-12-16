# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
tot_sum=0
for i in range(n):
    number=int(input())
    tot_sum=tot_sum+number
tot_sum_str=str(tot_sum)
print(tot_sum_str[0:10])
