# from collections import Counter
# n = int(input())
# vals = list(map(int,input().split()))
# data = dict(Counter(vals))

# data_val = data.values()
# print(data_val)

# TCS NQT 
def get_factors(n):
    return set([i for i in range(1,n+1) if n%i==0])

n =int(input())
m =int(input())
print(max(get_factors(n)&get_factors(m)))

# TCS NQT
times = [int(input()) for _ in range(4)]
x = int(input())
h,m,h1,m1 = times
correct_time = (h1,m1)
time_after_x = (h+x,m)
print(time_after_x, correct_time)
print((correct_time[1]-time_after_x[1]+abs(correct_time[0]-time_after_x[0])*60)*-1)