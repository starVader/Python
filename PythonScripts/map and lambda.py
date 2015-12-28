def fibn(N):
    result = [] 
    a,b = 0,1
    i = 0
    while( i < N):
        
        result.append(a)
        a,b = b,a+b
        i = i + 1
    return result
N = int(raw_input())
final = []
mylist =fibn(N)
print list(map(lambda i: i*i*i,mylist))
