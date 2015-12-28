# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
S = str(raw_input())
print "true"
slist = Counter(S).keys()
plist =  Counter(S).values()
print plist
for i in range(3):
    maxcount = max(plist)
    index = plist.index(maxcount)
    print slist[index],maxcount
    plist.remove(plist[index])
    slist.remove(slist[index])
    
        
    
    
