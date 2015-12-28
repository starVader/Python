K = int(raw_input())
if (0 < K < 1000):
    mylist =(map(int,raw_input().split()))
    for i in mylist:
        captain= mylist.count(i)
        if(captain == 1):
            print i
            break
    
    
