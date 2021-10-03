# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Blood:
    def __init__(self, bloodgrp,unit):
        self.bloodgrp=bloodgrp.upper()
        self.unit=unit
class Bloodbank:
    def __init__(self, bloodlst):
        self.bloodlst=bloodlst
    def isBloodAvailable(self, grp, unit):
        grp=grp.upper()
        return len(list(filter(lambda x:x.bloodgrp==grp and x.unit>=unit, self.bloodlst)))!=0
    def findMinBloodStock(self):
        m=min(self.bloodlst, key=lambda x:x.unit)
        return list(filter(lambda x:x.unit==m.unit,self.bloodlst))
n=int(input())
blood_objects=[]
for _ in range(n):
    grp, unit=input(), int(input())
    blood_objects.append(Blood(grp, unit))
check_grp=input()
check_unit=int(input())
bank = Bloodbank(blood_objects)
print("Blood Available" if bank.isBloodAvailable(check_grp, check_unit) else 'Blood Not Available')
[print(b.bloodgrp) for b in bank.findMinBloodStock()]