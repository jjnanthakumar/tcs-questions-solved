# Author : TechStact (Nanthakumar J J)

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

store = {
    101: ["Milk", 42, 10],
    102: ["Cheese", 50, 20],
    103: ["Ghee", 500,40],
    104: ["Bread", 40, 16]
}

item = int(input())
quantity = int(input())
if (store.get(item) is None):
    print("INVALID INPUT")
else:
    if (quantity<store[item][-1]):
        print("{:.1f} INR".format(store[item][1]*quantity))
        store[item][-1] -= quantity
        print(f"{store[item][-1]} LEFT")
    elif store[item][-1]<quantity:
        print("NO STOCK")
        print(f"{store[item][-1]} LEFT")