# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


s = input()
c = input()[:1]
n = int(input())
words = s.split()
print("Count of words found =",sum(i.count(c)==n for i in words))