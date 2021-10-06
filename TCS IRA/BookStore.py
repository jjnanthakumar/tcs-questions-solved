# Author : Nanthakumar J J

# Website : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

class Book:
    def __init__(self, id, bookName, authorName, type, price):
        self.id = id
        self.bookName = bookName
        self.authorName = authorName
        self.type = type
        self.price = price

    def discount(self, percentage):
        self.price = self.price - ((self.price*percentage)//100)

class BookStore:
    def __init__(self, bookObjs, ratings):
        self.bookObjs = bookObjs
        self.ratings = ratings

    def filterBooks(self, type):
        filtered = []
        for x in self.bookObjs:
            if x.type.lower() == type.lower() and (self.ratings.get(x.authorName) is not None) and (self.ratings.get(x.authorName) > 4):
                if x.type.lower() == "fiction":
                    x.discount(20)
                else:
                    x.discount(10)
                filtered.append(x)
        return filtered or None

    # Return Dictionary after applying dictionaries and counting books
    def getCount(self, price):
        data = {}
        for obj in self.bookObjs:
            if obj.price < price:
                if obj.type == "fiction":
                    obj.discount(20)
                else:
                    obj.discount(10)
                data[obj.authorName] = data.get(obj.authorName, 0)+1
        return data or None

# Main Code
n = int(input())
bookObjects = [Book(int(input()), input(), input(), input(), int(input())) for _ in range(n)]
ratings = {input(): float(input()) for _ in range(3)}
store = BookStore(bookObjects, ratings)
type = input()
price = int(input())
res = store.filterBooks(type)

print("Book Not Found." if res is None else "\n".join(f"{o.price}\n{o.bookName}" for o in res))

res1 = store.getCount(price)
print("Book is Unavailable." if res1 is None else "\n".join(f"{k} {v}" for k, v in res1.items()))
