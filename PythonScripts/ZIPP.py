N,X = map(int,raw_input().split())
count = 0
mylist =[]
result =[]
if (0 < N <=100)&(0 < X <= 100):
    sets = [set() for i in range(X)]
    while (count < X):
        sets[count] = (map(float,raw_input().split()))
        print sets[count]
        count = count + 1
    print zip(sets[0],sets[1],sets[2])
    
    
        
        
    
