# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

str1,str2=input(),input()
c=input().lower()[:1]

s1_char_freq = str1.lower().count(c)
s2_char_freq = str2.lower().count(c)
if s1_char_freq>s2_char_freq:
    print(str1)
    print(s1_char_freq)
elif s1_char_freq<s2_char_freq:
    print(str2)
    print(s2_char_freq)
else:
    print("Both strings have same frequency of given character")
    print(s1_char_freq)

