# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Product:
    def __init__(self,productName,productType,productPrice, quantityOnHand, reorderingQuantity):
        self.productName=productName
        self.productType=productType
        self.productPrice=productPrice
        self.quantityOnHand=quantityOnHand
        self.reorderingQuantity=reorderingQuantity

def findAvailableStock(productLists,productNames):
    actualData=list(filter(lambda x:x.productName in productNames,productLists))
    if not actualData:
        return None
    else:
        return {data.productName:data.quantityOnHand for data in actualData}
    
def updateStockByProductType(productLists,quantity,type):
    products=list(filter(lambda x:x.productType==type,productLists))
    if not products:
        return None
    else:
        for p in products:
            if not p.quantiyOnHand>p.reorderingQuantity:
                p.quantityOnHand+=quantity
        return products
n=5
productLists=[Product(input(),input(),int(input()),int(input()),int(input())) for i in range(n)]
countNames=int(input())
productNames=[input() for i in range(countNames)]    
quantity=int(input())
type=input()
data=findAvailableStock(productLists,productNames) 
if data is None:
    print('Product Not Found')
else:
    print(data)
    for k,v in data.items():
        print(f'{k} {v}')





        