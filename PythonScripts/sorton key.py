# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M = map(int,raw_input().split())
mylist =[]
temp =[]
for i in range(N):
    temp = map(int,raw_input().split())
    mylist.append(temp)
    mylist.sort(key = lambda pair: pair[1])
for i in mylist:
    print ' '.join(map(str, i))
                
# sort in nested list with second element of first sublist as key
