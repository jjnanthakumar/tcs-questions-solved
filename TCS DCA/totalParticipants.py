# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


n = int(input())
if n&1:
    res = [str(n//4) if i!=3 else str((n//4)+n%4) for i in range(4)]
else:
    res = [str(n//4) for _ in range(4)]

print("\n".join(res))