# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Apparel:
    def __init__(self, apparelbrand, type, price, inStock):
        self.apparelbrand = apparelbrand
        self.type = type
        self.price = price
        self.inStock = inStock


class Store:
    def __init__(self, apparelList):
        self.apparelList = apparelList

    def checkApparelAvailability(self, brand, type, apparelsize, noofapparel):
        check = list(filter(lambda x: brand ==
                            x.apparelbrand and type == x.type, self.apparelList))
        if not check:
            return False,None
        apparel = check[0]
        if apparel.inStock.get(apparelsize) is None or noofapparel > apparel.inStock.get(apparelsize):
            return False,None
        apparel.inStock[apparelsize] -= noofapparel
        return True,apparel


n = int(input())
ApparelObjects = []
for _ in range(n):
    brand = input()
    type = input()
    price = int(input())
    inStock = {}
    countinStock = int(input())
    for _ in range(countinStock):
        size=input()
        inStock[size] = int(input())
    ApparelObjects.append(Apparel(brand,type,price,inStock))
brand=input()
type=input()
size=input()
availability=int(input())
store=Store(ApparelObjects)
checker=store.checkApparelAvailability(brand,type,size,availability)
if(checker[0]):
    print("Size is Available")
    print('\n'.join(f'{k}:{v}' for k,v in checker[1].inStock.items()))
else:
    print("Size is not available")
    print("Apparel not found")


