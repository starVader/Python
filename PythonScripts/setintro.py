from __future__ import division
N = int(raw_input())
average = 0
sumc = 0
if (N <= 100):
    mylist = (map(int,raw_input().split()))
    mylist_new = list(set(mylist))
    for i in mylist_new:
        sumc = sumc + i
    average = sumc/(len(mylist_new))
    print  "%.3f"%average
