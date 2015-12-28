from collections import Counter
X = int(raw_input())
size = list(map(int,raw_input().split()))
index = 0
print Counter(size)
slist = Counter(size).keys()
plist =  Counter(size).values()
print slist
print plist
N = int(raw_input())
tamount = 0
for i in range(N):
    shsize,price = map(int,raw_input().split())
    if shsize in slist:
        index = slist.index(shsize)
        if plist[index] != 0:
            tamount = tamount + price
            plist[index] = (plist[index] - 1)

print tamount
    
