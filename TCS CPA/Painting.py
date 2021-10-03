# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Painting:
    def __init__(self, ID, Name, Price, Type):
        self.paintingId = ID
        self.painterName = Name
        self.paintingPrice = Price
        self.paintingType = Type


class ShowRoom:
    def __init__(self, paintingList):
        self.paintingObjects = paintingList

    def getTotalPaintingPrice(self, type):
        filtered = list(filter(lambda x: x.paintingType ==
                               type, self.paintingObjects))
        return None if not filtered else sum(map(lambda x: x.paintingPrice, filtered))

    def getPainterwithMaxCountOfPaintings(self):
        paintingDict = {}
        for painting in self.paintingObjects:
            paintingDict[painting.painterName] = paintingDict.get(
                painting.painterName, 0)+1
        return sorted(k for k, v in paintingDict.items() if v == max(paintingDict.values()))[0]


n = int(input())
paintingObj = [Painting(input(), input(), int(input()), input().lower()) 
for _ in range(n)]
type = input().lower()

Room = ShowRoom(paintingObj)
totPrice= Room.getTotalPaintingPrice(type)
print(totPrice if totPrice is not None else "Painting not found")
print(Room.getPainterwithMaxCountOfPaintings())

