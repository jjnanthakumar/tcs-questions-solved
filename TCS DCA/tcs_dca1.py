# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


# TCS DCA 1
data={str(i):str(j) for i,j in zip(range(0,10),range(9,-1,-1))}
n=int(input())
if n>=0 and n<=1000000:
    print(int(''.join(list(map(lambda x:data[x],str(n))))))
else:
    print("Wrong Input")

# Sample cases
# Input (integer)
# 105201
# Output (integer)
# 894798
