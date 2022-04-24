# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Boutique:
    def __init__(self,id_,name,type,rating,points):
        self.id=id_
        self.name=name
        self.type=type
        self.rating=rating
        self.points=points
    
class OnlineBoutique:
    def __init__(self,boutiqueDict):
        self.boutiqueDict=boutiqueDict

    def getboutique(self,lower_rating,upper_rating,extra_points,type):
        filteredBoutiques=self.boutiqueDict.get(type)
        if filteredBoutiques is not None:
            for obj in filteredBoutiques:
                if obj.rating>=lower_rating and obj.rating<=upper_rating:
                    obj.points+=extra_points
            return sorted(filteredBoutiques,key=lambda x: x.points,reverse=True)
        return None

# Driver Program
BoutiqueObjects={}
n=int(input())
for _ in range(n):
    boutiqueId=int(input())
    name=input()
    type=input().lower()
    rating=float(input())
    points=int(input())
    boutObject=Boutique(boutiqueId,name,type,rating,points)
    if type not in BoutiqueObjects.keys():
        BoutiqueObjects[type]=[boutObject]
    else:
        BoutiqueObjects[type].append(boutObject)

lower_rating=float(input())
upper_rating=float(input())
extra_points=int(input())
boutique_type=input().lower()

online = OnlineBoutique(BoutiqueObjects)
res=online.getboutique(lower_rating,upper_rating,extra_points,boutique_type)
if res is None:
    print("No boutique found")
else:
    for r in res:
        print(r.id,r.name,r.points)



        