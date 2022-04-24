# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


# TCS DCA 2
n=int(input())
data=[int(input()) for i in range(n)]
print(*list(filter(lambda x:x==1,data))+list(filter(lambda x:x==0,data))+list(filter(lambda x:x==2,data)))


# Sample cases
# Input (integer)
# 6
# 0
# 1
# 2
# 0
# 1
# 2
# Output (integer)
# 1 1 0 0 2 2
