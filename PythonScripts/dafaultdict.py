from collections import defaultdict
n,m = map(int,raw_input().split())
nlist = []
mlist = []
if(1 <= n <= 10000) & (1 <= m <=100):
    for i in range(n):
        nlist.append(raw_input())
    for i in range(m):
        mlist.append(raw_input())
    d = defaultdict(list)
    d['nlist'].append(nlist)
    d['mlist'].append(mlist)
    
