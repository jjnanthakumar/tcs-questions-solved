# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Property:
    def __init__(self,ptypenl,pvaluenl,mbpnl):
        self.property_type=ptypenl
        self.property_value=pvaluenl
        self.max_bid_price=mbpnl
class Tender:
    def __init__(self,bnamenl,ptypnl,bpnl):
        self.buyerName=bnamenl
        self.propertyType=ptypnl
        self.bidPrice=bpnl
def bidProperty(propObjects,tenderObjects):
    k=None
    filteredObjects=list(filter(lambda x: x.propertyType.lower() in list(map(lambda x:x.property_type.lower(),propObjects)),tenderObjects))
    for e in propObjects:
        for i in filteredObjects:
            if i.bidPrice<=e.max_bid_price and i.bidPrice>=e.property_value:
                print(i.buyerName)
                k=e
    for i in l1:
        if  k!=None and i.property_type==k.property_type:
            continue
        elif k!=None:
            print(i.property_type)
    if k==None:
            print("Property not found")
            for e in l1:
                print(e.property_type)
                
if __name__=='__main__':
    n=int(input())
    l1=[Property(input(),input(),int(input())) for _ in range(n)]
    n1=int(input())
    l2=[Tender(input(),input(),int(input())) for _ in range(n1)]
    bidProperty(l1,l2)
        
